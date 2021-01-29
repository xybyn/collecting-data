from CollectionProcessingPipeline import CollectionProcessingPipeline
from utils import *
from openpyxl import *

class MicceduParser:
    def __init__(self):
        self.root_url = r"http://indicators.miccedu.ru/monitoring/?m=vpo"

    def get_archives_links(self):
        url = r"http://indicators.miccedu.ru/monitoring/?m=vpo"
        hrefs = get_hrefs(url)
        return extract_data_from_collection(hrefs, ".*monitoring..*")

    def get_district_and_area_links(self, link):
        # избавляемся от лишних символов 'index.php?...'
        cleared_link = link[:link.rfind('/')]
        hrefs = get_hrefs(link)
        if self.get_archive_year(link) == '2015':
            return [f"{cleared_link}/{region_link}" for region_link in extract_data_from_collection(hrefs, "material\.php.*")]
        return [f"{cleared_link}/{region_link}" for region_link in extract_data_from_collection(hrefs, "\_vpo.*")]

    def extract_district_links(self, district_and_area_links):
        return extract_data_from_collection(district_and_area_links, ".*type\=1.*")

    def extract_area_links(self, district_and_area_links):
        return extract_data_from_collection(district_and_area_links, ".*type\=2.*")

    def get_archive_year(self, archive_link):
        result = re.match(".*20\d{2}", archive_link).group(0)
        return result.split('/')[-1]

    def get_institutes_with_data(self, link):
        page = requests.get(link)
        page.encoding = 'windows-1251'

        soup = BeautifulSoup(page.text, "html.parser")
        # сначала находим все элементы с тэгом tr, у которых есть дочерний элемент
        # td с классом inst. Так как tr с данными о университете не отличается от других
        # tr, то найдем сначала все дочерние элементы, так как мы точно знаем что tr будет содержать
        # элемент с тэгом td и классом inst, то находим сначала td с классом inst, потом извлекаем
        # родителя
        # Этот найденный td содержит информацию о названии
        # университета, так же данные по каждому из направлений

        #выбираем таблицу с классом an, так как есть еще одна таблица
        #с университетами, не прошедшими аттестацию, они отображаются в
        # таблице с классом ifail
        table_with_data = soup.find("table", {"class":"an"})
        whole_rows = [inst.parent for inst in table_with_data.find_all('td', {"class": "inst"})]
        institutes_with_data = []
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