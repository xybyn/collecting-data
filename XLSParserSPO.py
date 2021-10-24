import json

from xlrd import XLRDError

from modelsSPO import *
from utils import *


class XLSParserSPO:
    def __init__(self):
        self.P2_1_1 = "Р2_1_1"
        self.P2_1_2_1 = "Р2_1_2(1)"
        self.P2_1_2 = "Р2_1_2"
        self.P2_1_2_4 = "Р2_1_2 (4)"
        self.P2_1_4_1 = "Р2_1_4(1)"
        self.P2_1_4_2 = "Р2_1_4(2)"
        self.P2_1_2_2 = "Р2_1_2_П"
        self.P2_7 = "Р2_7"

    def parse_p2_1_1(self, xls_path):
        try:
            sheet = open_book_sheet(xls_path, self.P2_1_1)
        except XLRDError:
            print(f"Sheet {self.P2_1_1} is absent")
            return

        result = []

        try:
            start = sheet.col_values(1).index(1)
            end = sheet.col_values(1).index(7)
        except ValueError:
            print(f"Sheet {self.P2_1_1} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP211SPO(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10], row[11], row[12], row[13], row[14], row[15])

            if row[2] != 0:
                result.append(table_row)

        return result

    def parse_p2_1_2_1(self, xls_path):
        try:
            sheet = open_book_sheet(xls_path, self.P2_1_2_1)
        except XLRDError:
            print(f"Sheet {self.P2_1_2_1} is absent")
            return

        result = []

        try:
            start = sheet.col_values(1).index(1)
            end = sheet.col_values(1).index(11)
        except ValueError:
            print(f"Sheet {self.P2_1_2_1} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP2121SPO(row[0], row[1], row[2])

            if row[2] != 0:
                result.append(table_row)

        return result

    def parse_p2_1_2_4(self, xls_path):
        try:
            sheet = open_book_sheet(xls_path, self.P2_1_2_4)
        except XLRDError:
            print(f"Sheet {self.P2_1_2_4} is absent")
            return

        result = []

        try:
            start = sheet.col_values(1).index(1)
            end = sheet.col_values(1).index(11)
        except ValueError:
            print(f"Sheet {self.P2_1_2_4} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP2124SPO(row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                         row[10], row[11], row[12], row[13], row[14])

            if row[2] != 0:
                result.append(table_row)

        return result

    def parse_p2_1_4_1(self, xls_path):
        try:
            sheet = open_book_sheet(xls_path, self.P2_1_4_1)
        except XLRDError:
            print(f"Sheet {self.P2_1_4_1} is absent")
            return

        result = []

        try:
            start = sheet.col_values(1).index(1)
            end = len(sheet.col_values(1)) - 1
        except ValueError:
            print(f"Sheet {self.P2_1_4_1} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP2141SPO(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                         row[10])

            if row[2] != 0:
                result.append(table_row)

        return result

    def parse_p2_1_4_2(self, xls_path):
        try:
            sheet = open_book_sheet(xls_path, self.P2_1_4_2)
        except XLRDError:
            print(f"Sheet {self.P2_1_4_2} is absent")
            return

        result = []

        try:
            start = sheet.col_values(1).index(1)
            end = len(sheet.col_values(1)) - 1

        except ValueError:
            print(f"Sheet {self.P2_1_4_2} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP2142SPO(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                         row[10])

            if row[2] != 0:
                result.append(table_row)

        return result

    def export_year_to_json(self, path, year, json_path):
        json_year = YearSPO(year)

        for dirname, dirnames, filenames in os.walk(path):

            for filename in filenames:

                if "очная.xls" in filename and "заочная.xls" not in filename:
                    print(filename)
                    area = AreaSPO(filename.removesuffix('_ГОС_очная.xls'))

                    area.p211 = XLSParserSPO().parse_p2_1_1(os.path.join(dirname, filename))
                    area.p2121 = XLSParserSPO().parse_p2_1_2_1(os.path.join(dirname, filename))
                    area.p2124 = XLSParserSPO().parse_p2_1_2_4(os.path.join(dirname, filename))
                    area.p2141 = XLSParserSPO().parse_p2_1_4_1(os.path.join(dirname, filename))
                    area.p2142 = XLSParserSPO().parse_p2_1_4_2(os.path.join(dirname, filename))

                    json_year.areas.append(area)

                    json_text = json.dumps(json_year, ensure_ascii=False, default=my_default_SPO)
                    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
                    r = requests.post("http://192.168.0.12:8080/load/newspo", data=json_text.encode('utf-8'),
                                      headers=headers)
                    print(r.status_code, r.reason)

                    json_year.areas.clear()




    def parse_p2_1_1_old(self, xls_path):
        try:
            sheet = open_book_sheet(xls_path, self.P2_1_1)
        except XLRDError:
            print(f"Sheet {self.P2_1_1} is absent")
            return

        result = []

        try:
            start = sheet.col_values(1).index(1)
            end = sheet.col_values(1).index(3)
        except ValueError:
            print(f"Sheet {self.P2_1_1} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP211OldSPO(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                           row[9], row[10])

            if row[2] != 0:
                result.append(table_row)

        return result

    def parse_p2_1_2_old(self, xls_path):
        try:
            sheet = open_book_sheet(xls_path, self.P2_1_2)
        except XLRDError:
            print(f"Sheet {self.P2_1_2} is absent")
            return

        result = []

        try:
            start = sheet.col_values(1).index(1)
            end = sheet.col_values(1).index(4)
        except ValueError:
            print(f"Sheet {self.P2_1_2} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP212OldSPO(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                           row[9], row[10], row[11], row[12], row[13], row[14], row[15])

            if row[2] != 0:
                result.append(table_row)

        return result

    def parse_p2_1_2_2_old(self, xls_path):
        try:
            sheet = open_book_sheet(xls_path, self.P2_1_2_2)
        except XLRDError:
            print(f"Sheet {self.P2_1_2_2} is absent")
            return

        result = []

        try:
            start = sheet.col_values(1).index(1)
            end = sheet.col_values(1).index(4)
        except ValueError:
            print(f"Sheet {self.P2_1_2_2} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP2122OldSPO(row[0], row[1], row[2], row[3], row[4], row[5])

            if row[2] != 0:
                result.append(table_row)

        return result

    def parse_p2_7_old(self, xls_path):
        try:
            sheet = open_book_sheet(xls_path, self.P2_7)
        except XLRDError:
            print(f"Sheet {self.P2_7} is absent")
            return

        result = []

        try:
            start = sheet.col_values(1).index(1)
            end = sheet.col_values(1).index(7)
        except ValueError:
            print(f"Sheet {self.P2_7} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP27OldSPO(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                           row[9], row[10], row[11], row[12], row[13], row[14])

            if row[2] != 0:
                result.append(table_row)

        return result

    def export_year_to_json_old(self, path, year, json_path):
        json_year = YearSPO(year)

        for dirname, dirnames, filenames in os.walk(path):

            for filename in filenames:

                if "Очная.xls" in filename and "Заочная.xls" not in filename:
                    print(filename)
                    area = AreaOldSPO(filename.removesuffix('_ГОС_Очная.xls'))

                    area.p211 = XLSParserSPO().parse_p2_1_1_old(os.path.join(dirname, filename))
                    area.p212 = XLSParserSPO().parse_p2_1_2_old(os.path.join(dirname, filename))
                    area.p2122 = XLSParserSPO().parse_p2_1_2_2_old(os.path.join(dirname, filename))
                    area.p27 = XLSParserSPO().parse_p2_7_old(os.path.join(dirname, filename))

                    json_year.areas.append(area)

                    json_text = json.dumps(json_year, ensure_ascii=False, default=my_default_SPO)
                    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
                    r = requests.post("http://192.168.0.12:8080/load/oldspo", data=json_text.encode('utf-8'),
                                      headers=headers)
                    print(r.status_code, r.reason)

                    json_year.areas.clear()


