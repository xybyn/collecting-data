from CollectionProcessingPipeline import CollectionProcessingPipeline
from utils import *
from openpyxl import Workbook
import json
from DataProcessingPipeline import *
from models import *

class GovEduParser:
    def __init__(self):
        self.root_url = r"https://edu.gov.ru/activity/statistics/secondary_prof_edu"

    def get_reports(self):
        soup = BeautifulSoup(get_page_html(self.root_url), "html.parser")
        link = 'https://docs.edu.gov.ru/document/'
        report_hashes = [re.sub(r'.*uids=', '', href['src']) for href in soup.find_all("iframe")]
        links = [link+report_hash for report_hash in report_hashes]
        return links

    def get_file_links(self, report_link):
        soup = BeautifulSoup(get_page_html(report_link), "html.parser")

        rows = soup.find_all('div', {"class" : "col-12"})
        links = []
        for row in rows[:-1]:
            inner_div = row.contents[1]
            file_type = inner_div.contents[1].contents[1].attrs['class'][2]
            download_link = inner_div.contents[3].attrs['href']
            if 'zip' in file_type:
                links.append({"type" : "zip",
                              "link" : download_link})
            else:
                links.append({"type": "xls",
                              "link": download_link})

        return links

    def download_all(self, save_path):
        report_links = self.get_reports()
        for i in range(0, len(report_links)):
            folder_name = f"folder {i + 1}"
            os.mkdir(folder_name)

            files = self.get_file_links(report_links[i])
            for file in files:
                download_typed_file_by_link(file['link'][:-1], os.path.join(save_path, folder_name), file['type'])


