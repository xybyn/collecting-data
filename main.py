from bs4 import BeautifulSoup
import requests
import re
import os
import urllib.request
from DataProcessingPipeline import *
from CollectionProcessingPipeline import *
from utils import *

from openpyxl import *
def get_hrefs(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    hrefs = [a['href'] for a in soup.find_all('a', href=True)]
    return hrefs


def extract_data_from_collection(hrefs, pattern):
    result = []

    for href in hrefs:
        regex_result = re.match(pattern, href)
        if regex_result is not None:
            result.append(regex_result.group(0))
    return result


def get_file_name(file_path):
    split_path = file_path.split('/')
    return split_path[-1]


def download_file(url_origin, file_path_on_site, path_to_save):
    file_name = get_file_name(file_path_on_site)
    save_path = os.path.join(path_to_save, file_name)
    full_file_path_on_site = f"{url_origin}{file_path_on_site}"
    print(f"downloading: {file_name}")
    urllib.request.urlretrieve(full_file_path_on_site, save_path)


# TODO: make parallel
def download_files(url_origin, file_paths_on_site, path_to_save):
    for file_path_on_site in file_paths_on_site:
        download_file(url_origin, file_path_on_site, path_to_save)


def minobr_facade():
    url_origin = "https://minobrnauki.gov.ru"
    url = "https://minobrnauki.gov.ru/action/stat/highed/";
    current_directory = os.getcwd()
    path_to_save = current_directory

    hrefs = get_hrefs(url)
    file_paths_vpo1 = extract_data_from_collection(hrefs, ".*VPO.1.*(rar|zip)")
    file_paths_vpo2 = extract_data_from_collection(hrefs, ".*VPO.2.*(rar|zip)")
    download_files(url_origin, file_paths_vpo1, path_to_save)
    download_files(url_origin, file_paths_vpo2, path_to_save)


def get_archives_links():
    url = r"http://indicators.miccedu.ru/monitoring/?m=vpo"
    hrefs = get_hrefs(url)
    return extract_data_from_collection(hrefs, ".*monitoring..*")


def get_district_and_area_links(link):
    # избавляемся от лишних символов 'index.php?...'
    cleared_link = link[:link.rfind('/')]
    hrefs = get_hrefs(link)
    return [f"{cleared_link}/{region_link}" for region_link in extract_data_from_collection(hrefs, "\_vpo.*")]


# type1 округ (обобщенные данные) district
# type2 область (конкретные данные) area
def extract_district_links(district_and_area_links):
    return extract_data_from_collection(district_and_area_links, ".*type\=1.*")


def extract_area_links(district_and_area_links):
    return extract_data_from_collection(district_and_area_links, ".*type\=2.*")


def get_archive_year(archive_link):
    result = re.match(".*20\d{2}", archive_link).group(0)
    return result.split('/')[-1]


def get_row(row_html):
    pass

def get_institutes_with_data(link):
    page = requests.get(link)
    page.encoding = page.apparent_encoding

    soup = BeautifulSoup(page.text, "html.parser")
    a = soup.prettify()

    whole_rows = [inst.parent for inst in  soup.find_all('td', {"class":"inst"})]
    institutes_with_data = {}
    for row in whole_rows:
        institute = row.find("td", {"class": "inst"}).find("a").text
        data = [td.text for td in  row.find_all("td", {"class":"dkont"})]
        institutes_with_data[institute] = data
    return institutes_with_data

def get_table_headers(link):
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


def get_table(link):
    headers = get_table_headers(link)
    institutes = get_institutes_with_data(link)

    return {"headers" : headers, "institutes" : institutes}


def miccedu_facade():
    wb = Workbook()
    ws = wb.active
    archive_links = get_archives_links()[0]
    for archive_link in archive_links:
        district_and_area_links = get_district_and_area_links(archive_link)

        archive_year = get_archive_year(archive_link)
        ws.append([archive_year])
        for area in extract_area_links(district_and_area_links):
            result = get_table(area)
            ws.append(['университет'] + result['headers'])
            for key in result['institutes']:
                ws.append([key] + result['institutes'][key])
            wb.save(os.path.join(os.getcwd(), "test.xlsx"))
    pass


def main():
    miccedu_facade()
    #minobr_facade()
    #result = get_table("http://indicators.miccedu.ru/monitoring/2018/_vpo/material.php?type=2&id=10501");


main()
