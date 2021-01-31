from CollectionProcessingPipeline import CollectionProcessingPipeline
from utils import *
from openpyxl import *


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

    def export_to_excel(self, archive_link, path):
        district_and_area_links = self.get_district_and_area_links(archive_link)
        wb = Workbook()
        ws = wb.active
        area_links = self.extract_area_links(district_and_area_links)
        ws.append([self.get_archive_year(archive_link)] + self.get_table_headers(area_links[0]))
        for area_link in area_links:
            print(f"downloading data from {area_link}")
            institutes = self.get_institutes_with_data(area_link)
            for institute in institutes:
                ws.append(institute)

        wb.save(path)

    def export_all_data_to_excel(self, path):
        wb = Workbook()
        ws = wb.active
        for archive_link in self.get_archives_links():
            district_and_area_links = self.get_district_and_area_links(archive_link)
            archive_year = self.get_archive_year(archive_link)
            area_links = self.extract_area_links(district_and_area_links)
            ws.append([archive_year] + self.get_table_headers(area_links[0]))
            for area_link in area_links:
                print(f"downloading data from {area_link}")
                institutes = self.get_institutes_with_data(area_link)
                for institute in institutes:
                    ws.append(institute)

        wb.save(path)

    def get_institute_links(self, soup, area_link):
        hrefs = get_hrefs(soup)
        cleared_area_link = re.match(".*vpo", area_link)
        if (cleared_area_link is None):
            cleared_area_link = re.match(".*20\d\d", area_link)
        cleared_area_link = cleared_area_link.group(0)
        institute_links = [f"{cleared_area_link}/{link}" for link in extract_data_from_collection(hrefs, r"inst\..*")]
        return institute_links

    # napde id result

    def get_institute_indicators_and_values(self, soup):
        tables = get_table_by_class(soup, "napde")
        result_table = list()

        for table in tables:
            table_data = table.find_all("td", "n")

            for row in table_data:
                result_table.append([row.text, row.findNext('td').findNext('td').text+f" {row.findNext('td').text}"])

        return result_table

    def get_general_institute_indicators_and_values(self, soup):
        general_tables = get_table_by_id(soup, "result")
        result_table = list()

        for table in general_tables:
            table_data = table.find_all("td", "n")

            for row in table_data:
                result_table.append([row.text, row.findNext('td').text])

        return result_table

#analis_dop
    def get_addition_characteristics(self, soup):
        addition_tables = get_table_by_id(soup, "analis_dop")
        result_table = list()

        for table in addition_tables:
            table_data = table.find_all("td", "n")

            for row in table_data:
                result_table.append([row.text, row.findNext('td').findNext('td').text+f" {row.findNext('td').text}"])

        return result_table


    def export_to_excel(self, path):
        wb = Workbook()

        archive_links = self.get_archives_links()
        for archive_link in archive_links:
            archive_year = self.get_archive_year(archive_link)
            print(f"current year {archive_year}")
            wb.create_sheet(archive_year)
            current_ws = wb.get_sheet_by_name(archive_year)
            districts_and_area_links = self.get_district_and_area_links(archive_link)
            for area in self.extract_area_links(districts_and_area_links):
                print(f"area {area}")
                institute_links = self.get_institute_links(area)
                for institute_link in institute_links:
                    print(f"downloading {institute_link}")
                    current_ws.append(["ОБЩИЕ ПОКАЗАТЕЛИ И ЗНАЧЕНИЯ"])
                    general_indicators_and_values = self.get_general_institute_indicators_and_values(institute_link)
                    for item in general_indicators_and_values:
                        current_ws.append(item)

                    current_ws.append(["ПОКАЗАТЕЛИ И ЗНАЧЕНИЯ"])
                    indicators_and_values = self.get_institute_indicators_and_values(institute_link)

                    for item in indicators_and_values:
                        current_ws.append(item)
                    current_ws.append(["ДОПОЛНИТЕЛЬНЫЕ ХАРАКТЕРИСТИКИ"])

                    addition_characteristics = self.get_addition_characteristics(institute_link)

                    for item in addition_characteristics:
                        current_ws.append(item)

    def get_institute_name(self, soup, institute_link):
        table = get_table_by_id(soup, "info")[0]
        return table.b.text

    def export_area_to_excel(self, path, area):
        wb = Workbook()
        wb.create_sheet("2019")
        current_ws = wb["2019"]
        print(f"area {area}")
        institute_links = self.get_institute_links(area)
        for institute_link in institute_links:
            print(f"downloading {institute_link}")
            soup = BeautifulSoup(get_page_html(institute_link), "html.parser")
            institute_name = self.get_institute_name(soup, institute_link)
            general_indicators_and_values = self.get_general_institute_indicators_and_values(soup)
            current_ws.append([f"УНИВЕРСИТЕТ {institute_name}"])
            current_ws.append(["ОБЩИЕ ПОКАЗАТЕЛИ И ЗНАЧЕНИЯ"])
            for item in general_indicators_and_values:
                current_ws.append(item)

            current_ws.append(["ПОКАЗАТЕЛИ И ЗНАЧЕНИЯ"])
            indicators_and_values = self.get_institute_indicators_and_values(soup)

            for item in indicators_and_values:
                current_ws.append(item)
            current_ws.append(["ДОПОЛНИТЕЛЬНЫЕ ХАРАКТЕРИСТИКИ"])

            addition_characteristics = self.get_addition_characteristics(soup)

            for item in addition_characteristics:
                current_ws.append(item)

        wb.save(path)

    def get_area_name(self, area_soup):
        div = area_soup.find("div", {"id":"gerb"})
        return div.contents[3].text

    def export_year2_to_excel(self, path, link):
        wb = Workbook()
        wb.create_sheet("2019")
        current_ws = wb["2019"]
        district_and_areas = self.get_district_and_area_links(link)
        areas = self.extract_area_links(district_and_areas)
        for area in areas:
            print(f"area {area}")
            area_soup = BeautifulSoup(get_page_html(area), "html.parser")
            area_name = self.get_area_name(area_soup)
            institute_links = self.get_institute_links(area_soup, area)
            print(f"area {area_name}")
            for institute_link in institute_links:
                print(f"downloading {institute_link}")
                soup = BeautifulSoup(get_page_html(institute_link), "html.parser")
                institute_name = self.get_institute_name(soup, institute_link)
                general_indicators_and_values = self.get_general_institute_indicators_and_values(soup)
                current_ws.append([f"УНИВЕРСИТЕТ {institute_name}"])
                current_ws.append(["ОБЩИЕ ПОКАЗАТЕЛИ И ЗНАЧЕНИЯ"])
                for item in general_indicators_and_values:
                    current_ws.append(item)

                current_ws.append(["ПОКАЗАТЕЛИ И ЗНАЧЕНИЯ"])
                indicators_and_values = self.get_institute_indicators_and_values(soup)

                for item in indicators_and_values:
                    current_ws.append(item)
                current_ws.append(["ДОПОЛНИТЕЛЬНЫЕ ХАРАКТЕРИСТИКИ"])

                addition_characteristics = self.get_addition_characteristics(soup)

                for item in addition_characteristics:
                    current_ws.append(item)

        wb.save(path)
