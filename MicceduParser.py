from CollectionProcessingPipeline import CollectionProcessingPipeline
from utils import *
from openpyxl import Workbook
import json
from DataProcessingPipeline import *
from modelsVPO import *


class MicceduParser:
    def __init__(self):
        self.root_url = r"http://indicators.miccedu.ru/monitoring/?m=vpo"

    def get_archives_links(self):
        url = r"http://indicators.miccedu.ru/monitoring/?m=vpo"
        soup = BeautifulSoup(get_page_html(url), "html.parser")
        hrefs = get_hrefs(soup)
        return extract_data_from_collection(hrefs, ".*monitoring..*")

    def get_district_and_area_links(self, link):
        # избавляемся от лишних символов 'index.php?...'
        archive_year = int(self.get_archive_year(link))
        cleared_link = link
        if archive_year > 2015:
            cleared_link = link[:link.rfind('/')]

        soup = BeautifulSoup(get_page_html(link), "html.parser")
        hrefs = get_hrefs(soup)
        region_links = extract_data_from_collection(hrefs, "\_vpo.*")
        if len(region_links) == 0:
            region_links = extract_data_from_collection(hrefs, "material\.php.*")
        return [f"{cleared_link}/{region_link}" for region_link in region_links]

    def extract_district_links(self, district_and_area_links):
        return extract_data_from_collection(district_and_area_links, ".*type\=1.*")

    def extract_area_links(self, district_and_area_links):
        return extract_data_from_collection(district_and_area_links, ".*type\=2.*")

    def get_archive_year(self, archive_link):
        result = re.match(".*20\d{2}", archive_link).group(0)
        return result.split('/')[-1]

    def get_institutes_with_data(self, link):

        soup = BeautifulSoup(get_page_html(link), "html.parser")
        # сначала находим все элементы с тэгом tr, у которых есть дочерний элемент
        # td с классом inst. Так как tr с данными о университете не отличается от других
        # tr, то найдем сначала все дочерние элементы, так как мы точно знаем что tr будет содержать
        # элемент с тэгом td и классом inst, то находим сначала td с классом inst, потом извлекаем
        # родителя
        # Этот найденный td содержит информацию о названии
        # университета, так же данные по каждому из направлений

        # выбираем таблицу с классом an, так как есть еще одна таблица
        # с университетами, не прошедшими аттестацию, они отображаются в
        # таблице с классом ifail
        table_with_data = soup.find("table", {"class": "an"})
        whole_rows = [inst.parent for inst in table_with_data.find_all('td', {"class": "inst"})]
        institutes_with_data = list()
        for row in whole_rows:
            # находим краткое название университета во вложенном тэге a
            institute = row.find("td", {"class": "inst"}).find("a").text
            # собираем все данные со текущего ряда, dkont обозначает контейнер с данными
            data = [td.text for td in row.find_all("td", {"class": "dkont"})]
            institutes_with_data.append([institute] + data)

        return institutes_with_data

    def get_table_headers(self, link):
        page = requests.get(link)
        page.encoding = page.apparent_encoding
        soup = BeautifulSoup(page.text, "html.parser")
        theader_data = soup.find_all('thead')[0]
        table_headers = theader_data.contents[3].contents
        col_pipeline = CollectionProcessingPipeline(table_headers)
        col_pipeline \
            .add(remove_slash_n) \
            .add(remove_tags) \
            .add(strip) \
            .add(remove_dash_and_space) \
            .remove_empty()
        return col_pipeline.target_collection


    def get_institute_links(self, soup, area_link):
        hrefs = get_hrefs(soup)
        cleared_area_link = re.match(".*vpo", area_link)
        if (cleared_area_link is None):
            cleared_area_link = re.match(".*20\d\d", area_link)
        cleared_area_link = cleared_area_link.group(0)
        institute_links = [f"{cleared_area_link}/{link}" for link in extract_data_from_collection(hrefs, r"inst\..*")]
        return institute_links


    def get_institute_indicators_and_values(self, soup):
        tables = get_table_by_class(soup, "napde")
        if (tables is None):
            return [[]]
        result_table = list()

        for table in tables:
            table_data = table.find_all("td", "n")

            for row in table_data:
                result_table.append([row.text, row.findNext('td').findNext('td').text + f" {row.findNext('td').text}"])

        return result_table

    def get_general_institute_indicators_and_values(self, soup):
        general_tables = get_table_by_id(soup, "result")
        if (general_tables is None):
            return [[]]
        result_table = list()

        for table in general_tables:
            table_data = table.find_all("td", "n")

            for row in table_data:
                result_table.append([row.text, row.findNext('td').text])

        return result_table

    def get_addition_characteristics(self, soup):
        addition_tables = get_table_by_id(soup, "analis_dop")
        if(addition_tables is None):
            return []
        result_table = list()

        for table in addition_tables:
            table_data = table.find_all("td", "n")

            for row in table_data:
                result_table.append([row.text, row.findNext('td').findNext('td').text + f" {row.findNext('td').text}"])

        return result_table



    def get_institute_name(self, soup, institute_link):
        table = get_table_by_id(soup, "info")
        if table is None:
            return None
        return table[0].b.text


    def get_area_name(self, area_soup):
        div = area_soup.find("div", {"id": "gerb"})
        if div is None:
            table = get_table_by_style(area_soup, r"margin:40px 40px;")[0]
            return table.contents[1].text
        return div.contents[3].text



    def export_year_to_json(self, archive_link, path):
        year = self.get_archive_year(archive_link)
        new_year = Year(int(year))
        area_links = self.extract_area_links(self.get_district_and_area_links(archive_link))
        for area_link in area_links:
            area_soup = BeautifulSoup(get_page_html(area_link), "html.parser")
            area_name = DataProcessingPipeline(self.get_area_name(area_soup)) \
                .add(first_capital) \
                .target_string
            print(f"parsing area: {area_name}")

            new_area = Area(area_name)
            institute_links = self.get_institute_links(area_soup, area_link)
            for institute_link in institute_links:
                soup = BeautifulSoup(get_page_html(institute_link), "html.parser")
                temp = self.get_institute_name(soup, institute_link)
                if temp is None:
                    continue
                institute_name = DataProcessingPipeline(temp) \
                    .add(replace_brackets) \
                    .add(first_capital) \
                    .target_string

                print(f"parsing institute: {institute_name}")
                new_institute = Institute(institute_name)
                indicators_and_values = self.get_institute_indicators_and_values(
                    soup) + self.get_addition_characteristics(soup)
                for indicator in indicators_and_values:
                    indicator_name = DataProcessingPipeline(indicator[0]) \
                        .add(replace_brackets) \
                        .add(first_capital) \
                        .target_string
                    new_indicator = Indicator(indicator_name, indicator[1])
                    new_institute.indicators.append(new_indicator)
                directions = self.get_directions(soup)
                for direction in directions:
                    direction_name = DataProcessingPipeline(direction) \
                        .add(replace_brackets) \
                        .add(first_capital) \
                        .target_string
                    new_direction = Direction(direction_name)
                    new_institute.directions.append(new_direction)
                new_area.institutes.append(new_institute)
            new_year.areas.append(new_area)

        print("exporting...")
        json_text = json.dumps(new_year, ensure_ascii=False, default=my_default)
        file = open(path, "w", encoding="utf-8")
        file.write(json_text)
        file.close()

    def get_directions(self, soup):
        table = get_table_by_id(soup, "analis_reg")
        if len(table) == 0:
            table = get_table_by_id(soup, "trud")
            if len(table) == 0:
                return []

            rows = table[0].find_all("tr")[2:]
            tds = [row.find("td") for row in rows]
            directions = [td.text for td in tds if "class" in td.attrs]
            return directions

        table = table[0]

        rows = table.find_all("tr")[2:]
        directions = [row.find("td").text for row in rows]
        return directions
