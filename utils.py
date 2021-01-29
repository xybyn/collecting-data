import re
import urllib.request
import requests
from bs4 import BeautifulSoup
import os


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


def strip(string):
    return string.strip()


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
