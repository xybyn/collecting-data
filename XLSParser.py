import json
import os

import xlrd
from xlrd import XLRDError
from models import *


def open_book_sheet(xls_path, sheet):

    book = xlrd.open_workbook(xls_path)

    sheet = book.sheet_by_name(sheet)

    return sheet


class XLSParser:
    def __init__(self):
        self.P2_12 = "Р2_12"
        self.P2_1_1 = "Р2_1_1"
        self.P2_1_2_1 = "Р2_1_2(1)"
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
            end = sheet.col_values(0).index('Обучаются второй год на данном курсе, включая находящихся\r\nв академическом '
                                        'отпуске: из строки 03')
        except ValueError:
            print(f"Sheet {self.P2_1_2_1} is empty")
            return


        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP2121(row[3])

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
            end = sheet.col_values(0).index('Обучаются второй год на данном курсе, включая находящихся\r\nв академическом '
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
            end = sheet.col_values(0).index('Всего по программам бакалавриата, специалитета и магистратуры (сумма строк '
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

        result = []

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
                    result.append(table_row)

        return result

    def export_year_to_json(self, path, year, json_path):
        json_year = Year(year)

        codes = self.parse_p2_1_2_1(path + "/../СВОД_ВПО1_ГОС_очная.xls")

        for dirname, dirnames, filenames in os.walk(path):

            for filename in filenames:

                if "очная.xls" in filename and "заочная.xls" not in filename:
                    print(filename)
                    area = AreaVPO(filename.removesuffix('_ГОС_очная.xls'))
                    area.table_row_p12 = XLSParser().parse_p2_12(os.path.join(dirname, filename))

                    subjects = self.create_subject_list(codes, os.path.join(dirname, filename))

                    area.subjects = subjects

                    json_year.areas.append(area)

        json_text = json.dumps(json_year, ensure_ascii=False, default=my_default)
        file = open(json_path, "w", encoding="utf-8")
        file.write(json_text)
        file.close()

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

            subject = Subject(code.code,
                              table_row_2_1_1.budget_amount,
                              table_row_2_1_1.contract_amount,
                              table_row_2_1_1.total_fed_amount,
                              table_row_2_1_1.gr_contract_amount,
                              table_row_2_1_1.women_amount,
                              table_row_2_1_4.total_fed_amount,
                              table_row_2_1_4.contract_amount,
                              table_row_2_1_4.women_amount,
                              table_row_2_1_3.total_grad_amount,
                              table_row_2_1_3.magistracy_amount,
                              table_row_2_1_3.total_fed_amount,
                              table_row_2_1_3.contract_amount,
                              table_row_2_1_3.women_amount
                              )

            subjects.append(subject)

        return subjects

    def find_row_by_code(self, table, code):

        if table is None:
            return -1

        for row in table:
            if row.code == code.code:
                table_row = row
                return table_row

        return -1