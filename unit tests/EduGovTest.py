import os
import unittest
from GovEduParser import *
from utils import *

class GovEduParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = GovEduParser()

    def test_get_reports_should_return_12_links(self):
        links = self.parser.get_reports()
        self.assertEqual(len(links), 12)


    def test_download_all(self):
        save_path = os.getcwd()
        self.parser.download_all(save_path)



    def test_get_file_links_should_return_20_links(self):
        report_link = 'https://docs.edu.gov.ru/document/66efe5a01f0b8c2578af12f5710b02b4/'
        links = self.parser.get_file_links(report_link)
        self.assertEqual(len(links), 20)

    def test_download_files(self):
        report_link = 'https://docs.edu.gov.ru/document/66efe5a01f0b8c2578af12f5710b02b4/download/3412'

        file = {"type" : "xls", "link" : report_link}

        download_typed_file_by_link(file['link'], os.getcwd(), file['type'])


    def test_download_year(self):
        report_link = 'https://docs.edu.gov.ru/document/66efe5a01f0b8c2578af12f5710b02b4/'
        files = self.parser.get_file_links(report_link)
        for file in files:
            download_typed_file_by_link(file['link'], os.getcwd(), file['type'])





if __name__ == "__main__":
    unittest.main()
