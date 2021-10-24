import json

import xlrd
from xlrd import XLRDError

from modelsVPO import *
from utils import *
import requests


class XLSParser:
    def __init__(self):
        self.P2_12 = "Р2_12"
        self.P2_5 = "Р2_5"
        self.P2_10 = "Р2_10"
        self.P2_1_1 = "Р2_1_1"
        self.P2_1_2_1 = "Р2_1_2(1)"
        self.P2_1_2 = "Р2_1_2"
        self.P2_1_2P = "Р2_1_2_П"
        self.P2_1_2_4 = "Р2_1_2 (4)"
        self.P2_1_3 = "Р2_1_3(1)"
        self.graduation_type = ["Бакалавриат", "Специалитет", "Магистратура"]

    def parse(self, xls_path):
        self.parse_p2_1_1(xls_path)
        self.parse_p2_12(xls_path)
        self.parse_p2_1_2_4(xls_path)
        self.parse_p2_1_3(xls_path)
        self.parse_p2_1_2_1(xls_path)

    def parse_p2_1_1(self, xls_path):

        try:
            sheet = open_book_sheet(xls_path, self.P2_1_1)
        except XLRDError:
            print(f"Sheet {self.P2_1_1} is absent")
            return

        result = []

        try:
            start = sheet.col_values(0).index('Программы бакалавриата - всего')
            end = sheet.col_values(0).index('Всего по программам бакалавриата, специалитета и магистратуры\r\n(сумма '
                                            'строк 01, 02, 03)')
        except ValueError:
            print(f"Sheet {self.P2_1_1} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP211(row[2], row[3], row[6], row[9], row[15], row[16])

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
            start = sheet.col_values(0).index('Программы бакалавриата - всего')
            end = sheet.col_values(0).index(
                'Обучаются второй год на данном курсе, включая находящихся\r\nв академическом '
                'отпуске: из строки 03')
        except ValueError:
            print(f"Sheet {self.P2_1_2_1} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP2121(row[0], row[3])

            if row[3] != 0:
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
            start = sheet.col_values(0).index('Программы бакалавриата - всего')
            end = sheet.col_values(0).index(
                'Обучаются второй год на данном курсе, включая находящихся\r\nв академическом '
                'отпуске: из строки 03')
        except ValueError:
            print(f"Sheet {self.P2_1_2_4} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP2124(row[3], row[13], row[18], row[19])

            if row[3] != 0:
                result.append(table_row)

        return result

    def parse_p2_1_3(self, xls_path):

        try:
            sheet = open_book_sheet(xls_path, self.P2_1_3)
        except XLRDError:
            print(f"Sheet {self.P2_1_3} is absent")
            return

        result = []

        try:
            start = sheet.col_values(0).index('Программы бакалавриата - всего')
            end = sheet.col_values(0).index(
                'Всего по программам бакалавриата, специалитета и магистратуры (сумма строк '
                '01, 02, 03)')
        except ValueError:
            print(f"Sheet {self.P2_1_3} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP213(row[3], row[4], row[8], row[9], row[15], row[16])

            if row[3] != 0:
                result.append(table_row)

        return result

    def parse_p2_12(self, xls_path):

        book = xlrd.open_workbook(xls_path)

        book_sh_names = [name for name in book.sheet_names() if self.P2_12 in name]

        if len(book_sh_names) == 0:
            print(f"Sheets {self.P2_12} are absent")
            return

        result = [[], [], []]

        for i in range(0, 3):

            sheet = book.sheet_by_name(book_sh_names[i])

            try:
                start = sheet.col_values(0).index('Студенты, обучающиеся на условиях общего приема\r\n- всего (сумма '
                                                  'строк 02, 03, 04)')
                end = sheet.col_values(0).index('лица без гражданства')

            except ValueError:
                print(f"Sheet {self.P2_1_3} is empty")
                return

            for row_num in range(start, end + 1):
                row = sheet.row_values(row_num)

                table_row = TableRowP212(self.graduation_type[i], row[0], row[1], row[2], row[3], row[4], row[5],
                                         row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14],
                                         row[15], row[16], row[17])

                if row[2] != 0:
                    result[i].append(table_row)

        return result

    def export_year_to_json(self, path, year, json_path):
        json_year = Year(year)

        codes = self.parse_p2_1_2_1(path + "/../СВОД_ВПО1_ГОС_очная.xls")

        for dirname, dirnames, filenames in os.walk(path):

            for filename in filenames:

                if "очная.xls" in filename and "заочная.xls" not in filename:
                    print(filename)
                    area = AreaVPO(filename.removesuffix('_ГОС_очная.xls'))

                    table_p2_12 = XLSParser().parse_p2_12(os.path.join(dirname, filename))
                    area.bachelor = table_p2_12[0]
                    area.spec = table_p2_12[1]
                    area.magistracy = table_p2_12[2]

                    area.subjects = self.create_subject_list(codes, os.path.join(dirname, filename))

                    json_year.areas.append(area)

                    json_text = json.dumps(json_year, ensure_ascii=False, default=my_default)
                    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
                    r = requests.post("http://192.168.0.12:8080/load/newvpo", data=json_text.encode('utf-8'),
                                      headers=headers)
                    print(r.status_code, r.reason)

                    json_year.areas.clear()


    def create_subject_list(self, codes, path):

        subjects = []

        table_p_2_1_3 = XLSParser().parse_p2_1_3(path)
        table_p_2_1_1 = XLSParser().parse_p2_1_1(path)
        table_p_2_1_4 = XLSParser().parse_p2_1_2_4(path)

        for code in codes:
            table_row_2_1_3 = self.find_row_by_code(table_p_2_1_3, code)
            table_row_2_1_1 = self.find_row_by_code(table_p_2_1_1, code)
            table_row_2_1_4 = self.find_row_by_code(table_p_2_1_4, code)

            if table_row_2_1_3 == -1:
                table_row_2_1_3 = TableRowP213(code)

            if table_row_2_1_1 == -1:
                table_row_2_1_1 = TableRowP211(code)

            if table_row_2_1_4 == -1:
                table_row_2_1_4 = TableRowP2124(code)

            subjects.append(Subject(code.name, code.code, table_row_2_1_1, table_row_2_1_4, table_row_2_1_3))

        return subjects

    def find_row_by_code(self, table, code):

        if table is None:
            return -1

        for row in table:
            if row.code == code.code:
                table_row = row
                return table_row

        return -1

    def parse_p2_1_1_old(self, xls_path):

        try:
            sheet = open_book_sheet(xls_path, self.P2_1_1)
        except XLRDError:
            print(f"Sheet {self.P2_1_1} is absent")
            return

        result = []

        try:
            start = sheet.col_values(0).index('Программы бакалавриата - всего')
            end = sheet.col_values(0).index('Всего по программам высшего образования (сумма строк 01, 05, 09)')
        except ValueError:
            print(f"Sheet {self.P2_1_1} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowOldP211(row[0], row[2], row[3], row[5], row[8])

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
            start = sheet.col_values(0).index('Программы бакалавриата - всего')
            end = sheet.col_values(0).index('Всего по программам высшего образования (сумма строк 01, 06, 11)')
        except ValueError:
            print(f"Sheet {self.P2_1_2} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowOldP212(row[0], row[2], row[3], row[19], row[20])

            if row[2] != 0:
                result.append(table_row)

        return result

    def parse_p2_1_2p_old(self, xls_path):

        try:
            sheet = open_book_sheet(xls_path, self.P2_1_2P)
        except XLRDError:
            print(f"Sheet {self.P2_1_2P} is absent")
            return

        result = []

        try:
            start = sheet.col_values(0).index('Программы бакалавриата - всего')
            end = sheet.col_values(0).index('Всего по программам высшего образования (сумма строк 01, 06, 11)')
        except ValueError:
            print(f"Sheet {self.P2_1_2P} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowOldP212P(row[0], row[2], row[3], row[6], row[7], row[9])

            if row[2] != 0:
                result.append(table_row)

        return result

    def parse_p2_5_old(self, xls_path):

        try:
            sheet = open_book_sheet(xls_path, self.P2_5)
        except XLRDError:
            print(f"Sheet {self.P2_5} is absent")
            return

        result = []

        try:
            start = sheet.col_values(0).index('Прием')
            end = sheet.col_values(0).index('Выпуск')
        except ValueError:
            print(f"Sheet {self.P2_5} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowOldP25(row[0], row[6])

            result.append(table_row)

        return result

    def parse_p2_10_old(self, xls_path):

        try:
            sheet = open_book_sheet(xls_path, self.P2_10)
        except XLRDError:
            print(f"Sheet {self.P2_10} is absent")
            return

        result = []

        try:
            start = sheet.col_values(0).index('Студенты, обучающиеся на условиях общего приема - всего (сумма строк '
                                              '02, 03, 04)')
            end = sheet.col_values(0).index('Кроме того: Лица без гражданства, обучающиеся по международным '
                                            'договорам')
        except ValueError:
            print(f"Sheet {self.P2_10} is empty")
            return

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowOldP210(row[0], row[1], row[2], row[3], row[4], row[5],
                                        row[6], row[7], row[8], row[9], row[10], row[11])

            if row[2] != 0:
                result.append(table_row)

        return result

    def export_year_to_json_old(self, path, year, json_path):
        json_year = Year(year)

        codes = self.parse_p2_1_2_old(path + "/../СВОД_ВПО1_ГОС_очная.xls")

        for dirname, dirnames, filenames in os.walk(path):

            for filename in filenames:

                if "Очная.xls" in filename and "Заочная.xls" not in filename:
                    print(filename)
                    shortname = filename.removesuffix('_ГОС_Очная.xls')
                    shortname = shortname.removesuffix('_ГОС_Автономные_Очная.xls')
                    shortname = shortname.removesuffix('_ГОС_Бюджетные_Очная.xls')
                    shortname = shortname.removesuffix('_ГОС_Казенные_Очная.xls')
                    area = AreaOldVPO(shortname)

                    area.old_subjects = self.create_subject_list_old(codes, os.path.join(dirname, filename))

                    area.old_p25 = XLSParser().parse_p2_5_old(os.path.join(dirname, filename))
                    area.old_p210 = XLSParser().parse_p2_10_old(os.path.join(dirname, filename))

                    json_year.areas.append(area)

                    json_text = json.dumps(json_year, ensure_ascii=False, default=my_default)
                    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
                    r = requests.post("http://192.168.0.12:8080/load/oldvpo", data=json_text.encode('utf-8'),
                                      headers=headers)
                    print(r.status_code, r.reason)

                    json_year.areas.clear()



    def create_subject_list_old(self, codes, path):

        old_subjects = []

        table_p_2_1_2_old = XLSParser().parse_p2_1_2_old(path)
        table_p_2_1_2p_old = XLSParser().parse_p2_1_2p_old(path)
        table_p_2_1_1_old = XLSParser().parse_p2_1_1_old(path)

        for code in codes:
            table_row_p_2_1_2_old = self.find_row_by_code_old(table_p_2_1_2_old, code)
            table_row_p_2_1_2p_old = self.find_row_by_code_old(table_p_2_1_2p_old, code)
            table_row_p_2_1_1_old = self.find_row_by_code_old(table_p_2_1_1_old, code)

            if table_row_p_2_1_2_old == -1:
                table_row_p_2_1_2_old = TableRowOldP212(code.name, code.classification, code.code)

            if table_row_p_2_1_2p_old == -1:
                table_row_p_2_1_2p_old = TableRowOldP212P(code.name, code.classification, code.code)

            if table_row_p_2_1_1_old == -1:
                table_row_p_2_1_1_old = TableRowOldP211(code.name, code.code)

            old_subjects.append(OldSubject(code.name, code.code, code.classification,
                                           table_row_p_2_1_1_old, table_row_p_2_1_2_old,
                                           table_row_p_2_1_2p_old))

        return old_subjects

    def find_row_by_code_old(self, table, code):

        if table is None:
            return -1

        for row in table:
            if row.code == code.code:
                return row

        return -1
