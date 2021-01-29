from utils import *


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
        whole_rows = [inst.parent for inst in soup.find_all('td', {"class": "inst"})]
        institutes_with_data = []
        for row in whole_rows:
            # находим краткое название университета во вложенном тэге a
            institute = row.find("td", {"class": "inst"}).find("a").text
            # собираем все данные со текущего ряда, dkont обозначает контейнер с данными
            data = [td.text for td in row.find_all("td", {"class": "dkont"})]
            institutes_with_data.append([institute] + data)

        return institutes_with_data
