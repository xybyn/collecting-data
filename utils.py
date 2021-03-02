import re
import urllib.request
import zipfile

import requests
import xlrd
from bs4 import BeautifulSoup
import os
from threading import Thread
import gevent.monkey
import shutil

from pyunpack import Archive


def remove_substring(string, substring, replacement):
    if substring in string:
        return string.replace(substring, replacement)
    return string


def remove_slash_n(string):
    return remove_substring(string, '\n', ' ')


def remove_td(string):
    temp = remove_substring(string, '<td>', ' ')
    return remove_substring(temp, '</td>', ' ')


def remove_tags(string):
    return re.sub(r'<.*?>', ' ', str(string))


def remove_br(string):
    return re.sub(r'<br/>', ' ', str(string))


def remove_dash_and_space(string):
    return re.sub(r'-\ ', '', str(string))


def remove_dash(string):
    return remove_substring(string, '-', ' ')


def capitalize(string):
    return string.capitalize()


def replace_brackets(string):
    return re.sub('[«»]', '\"', string)


def lower(string):
    return string.lower()


def title(string):
    return string.title()


def first_capital(string):
    if len(string) > 1:
        return string[0].upper() + string[1:]
    if len(string) == 1:
        return string.upper()

    return string


def get_page_html(url):
    page = requests.get(url)
    page.encoding = 'windows-1251'
    return page.text


def strip(string):
    return string.strip()


def get_hrefs(soup):
    hrefs = [a['href'] for a in soup.find_all('a', href=True)]
    return hrefs


def get_tds(url, class_name):
    soup = BeautifulSoup(get_page_html(url), "html.parser")
    tds = soup.find_all('td', {"class": class_name})
    return tds


def get_table_by_class(soup, class_name):
    table = soup.find_all('table', {"class": class_name})
    return table


def get_table_by_style(soup, style):
    table = soup.find_all('table', {"style": style})
    return table


def get_table_by_id(soup, id):
    table = soup.find_all('table', {"id": id})
    return table


def extract_data_from_collection(hrefs, pattern):
    result = list()

    for href in hrefs:
        regex_result = re.match(pattern, href)
        if regex_result is not None:
            result.append(regex_result.group(0))
    return result


def get_file_name(file_path):
    if file_path.endswith('/'):
        file_path = file_path[:-1]
    split_path = file_path.split('/')
    return split_path[-1]


def download_file(url_origin, file_path_on_site, path_to_save):
    file_name = get_file_name(file_path_on_site)
    save_path = os.path.join(path_to_save, file_name)
    full_file_path_on_site = f"{url_origin}{file_path_on_site}"
    print(f"downloading: {file_name}")
    urllib.request.urlretrieve(full_file_path_on_site, save_path)
    print(f"downloaded: {file_name}")


def download_file_by_link(link, path_to_save):
    file_name = get_file_name(link) + ".xls"
    save_path = os.path.join(path_to_save, file_name)
    print(f"downloading: {file_name}")
    urllib.request.urlretrieve(link, save_path)
    print(f"downloaded: {file_name}")


def download_typed_file_by_link(link, path_to_save, type):
    file_name = get_file_name(link) + "." + type
    save_path = os.path.join(path_to_save, file_name)
    print(f"downloading: {file_name}")
    urllib.request.urlretrieve(link, save_path)
    print(f"downloaded: {file_name}")


def download_files(url_origin, file_paths_on_site, path_to_save):
    for file_path_on_site in file_paths_on_site:
        download_file(url_origin, file_path_on_site, path_to_save)


def download_files_in_parallel(url_origin, file_paths_on_site, path_to_save):
    threads = []
    for file_path_on_site in file_paths_on_site:
        thread = Thread(target=download_file, args=(url_origin, file_path_on_site, path_to_save))
        thread.start()

    for thread in threads:
        thread.join()


def download_files_async(url_origin, file_paths_on_site, path_to_save):
    gevent.monkey.patch_all()

    jobs = [gevent.spawn(download_file, url_origin, file_path_on_site, path_to_save) for file_path_on_site in
            file_paths_on_site]
    gevent.wait(jobs)


def unarchive(archives_path, path_to_save):
    archives = os.listdir(archives_path)
    for archive in archives:
        if archive.endswith(".zip") or archive.endswith(".rar"):
            os.mkdir(path_to_save + archive.removesuffix(".*(rar|zip)"))
            path = path_to_save + archive.removesuffix(".*(rar|zip)")
            unpack_zipfile(archives_path + archive, path, 'cp866')
            print(f"{archive} unarchived")


def unpack_zipfile(filename, extract_dir, encoding='cp437'):
    with zipfile.ZipFile(filename) as archive:
        for entry in archive.infolist():
            name = entry.filename.encode('cp437').decode(encoding)  # reencode!!!

            # don't extract absolute paths or ones with .. in them
            if name.startswith('/') or '..' in name:
                continue

            target = os.path.join(extract_dir, *name.split('/'))
            os.makedirs(os.path.dirname(target), exist_ok=True)
            if not entry.is_dir():  # file
                with archive.open(entry) as source, open(target, 'wb') as dest:
                    shutil.copyfileobj(source, dest)


def open_book_sheet(xls_path, sheet):
    book = xlrd.open_workbook(xls_path)

    sheet = book.sheet_by_name(sheet)

    return sheet
