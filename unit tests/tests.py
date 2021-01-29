import unittest
from MicceduParser import MicceduParser


class MicceduParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = MicceduParser()

    def test_get_archive_links_should_return_7_links(self):
        # arrange
        links = ['http://indicators.miccedu.ru/monitoring/2019/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2018/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2017/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2016/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2015/']
        # act
        results = self.parser.get_archives_links()
        # assert
        self.assertEqual(len(results), 7)
        for link in links:
            self.assertTrue(link in results)

    def test_extract_district_links_for_2019_should_return_8_links(self):
        # arrange
        links = ['http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=1',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=2',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=4',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=3',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=25',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=5',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=6',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=7'
                 ]
        district_and_area_links = self.parser.get_district_and_area_links(
            'http://indicators.miccedu.ru/monitoring/2019/index.php?m=vpo')
        # act
        results = self.parser.extract_district_links(district_and_area_links)

        # assert
        self.assertEqual(len(results), 8)
        for link in links:
            self.assertTrue(link in results)

    def test_extract_areas_links_for_2019_should_return_85_links(self):
        # arrange
        links = ['http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10501',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10903',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10706'
                 ]
        district_and_area_links = self.parser.get_district_and_area_links(
            'http://indicators.miccedu.ru/monitoring/2019/index.php?m=vpo')
        # act
        results = self.parser.extract_area_links(district_and_area_links)

        # assert
        self.assertEqual(len(results), 85)
        for link in links:
            self.assertTrue(link in results)

    def test_get_district_and_area_links_for_2019_should_return_93_links(self):
        # arrange
        links = ['http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10501',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10903',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10706'
                 ]
        # act
        results = self.parser.get_district_and_area_links(
            'http://indicators.miccedu.ru/monitoring/2019/index.php?m=vpo')
        # assert
        self.assertEqual(len(results), 93)
        for link in links:
            self.assertTrue(link in results)

    def test_get_archive_year(self):
        # arrange
        links = ['http://indicators.miccedu.ru/monitoring/2019/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2018/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2017/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2016/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2015/']

        years = ['2019',
                 '2018',
                 '2017',
                 '2016',
                 '2015']

        # act
        results = [self.parser.get_archive_year(link) for link in links]

        # assert
        for year in years:
            self.assertTrue(year in results)

    def test_get_institutes_with_data_for_2019_should_return_3_rows_10_columns(self):
        #arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10403'
        #action
        results = self.parser.get_institutes_with_data(test_link)
        #assert
        self.assertEqual(len(results), 3)
        self.assertEqual(len(results[0]), 10)
        self.assertEqual(results[0][3], '')
        self.assertEqual(results[1][2], '4018,7')
        self.assertEqual(results[2][8], '77,4')

    def test_get_institutes_with_data_for_2019_should_return_23_rows_10_columns(self):
        # arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10903'
        # action
        results = self.parser.get_institutes_with_data(test_link)
        # assert
        self.assertEqual(len(results), 23)
        self.assertEqual(len(results[0]), 10)

        self.assertEqual(results[10][0], 'федеральное государственное бюджетное образовательное учреждение высшего образования «Новосибирский государственный медицинский университет» Министерства здравоохранения Российской Федерации')
        self.assertEqual(results[22][5], '9')
        self.assertEqual(results[21][5], '3711,65')

    def test_get_institutes_with_data_for_2018_should_return_16_rows_10_columns(self):
        # arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2018/_vpo/material.php?type=2&id=11107'
        # action
        results = self.parser.get_institutes_with_data(test_link)
        # assert
        self.assertEqual(len(results), 16)
        self.assertEqual(len(results[0]), 10)

        self.assertEqual(results[10][0], 'Филиал АНО ВО "Московский институт государственного управления и права" в Республике Саха (Якутия)')
        self.assertEqual(results[0][5], '201')

    def test_get_institutes_with_data_for_2018_should_return_16_rows_10_columns(self):
        # arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2018/_vpo/material.php?type=2&id=11107'
        # action
        results = self.parser.get_institutes_with_data(test_link)
        # assert
        self.assertEqual(len(results), 16)
        self.assertEqual(len(results[0]), 10)

        self.assertEqual(results[10][0], 'Филиал АНО ВО "Московский институт государственного управления и права" в Республике Саха (Якутия)')
        self.assertEqual(results[0][5], '201')
if __name__ == "__main__":
    unittest.main()
