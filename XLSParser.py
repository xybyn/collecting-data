import json
import xlrd
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

    def parse(self, xls_path):
        self.parse_p2_1_1(xls_path)
        self.parse_p2_12(xls_path)
        self.parse_p2_1_2_4(xls_path)
        self.parse_p2_1_3(xls_path)
        self.parse_p2_1_2_1(xls_path)

    def parse_p2_1_1(self, xls_path):

        sheet = open_book_sheet(xls_path, self.P2_1_1)

        if sheet is None:
            return

        start = sheet.col_values(0).index('Программы бакалавриата - всего')
        end = sheet.col_values(0).index('Всего по программам бакалавриата, специалитета и магистратуры\r\n(сумма '
                                        'строк 01, 02, 03)')

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP211(row[0], row[2], row[3], row[6], row[9])

            json_text = json.dumps(table_row, ensure_ascii=False, default=my_default)
            print(json_text)

    def parse_p2_1_2_1(self, xls_path):

        sheet = open_book_sheet(xls_path, self.P2_1_2_1)

        if sheet is None:
            return

        start = sheet.col_values(0).index('Программы бакалавриата - всего')
        end = sheet.col_values(0).index('Обучаются второй год на данном курсе, включая находящихся\r\nв академическом '
                                        'отпуске: из строки 03')

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP2121(row[0], row[3])

            json_text = json.dumps(table_row, ensure_ascii=False, default=my_default)
            print(json_text)

    def parse_p2_1_2_4(self, xls_path):

        sheet = open_book_sheet(xls_path, self.P2_1_2_4)

        if sheet is None:
            return

        start = sheet.col_values(0).index('Программы бакалавриата - всего')
        end = sheet.col_values(0).index('Обучаются второй год на данном курсе, включая находящихся\r\nв академическом '
                                        'отпуске: из строки 03')

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP2124(row[0], row[13], row[18], row[19])

            json_text = json.dumps(table_row, ensure_ascii=False, default=my_default)
            print(json_text)

    def parse_p2_1_3(self, xls_path):

        sheet = open_book_sheet(xls_path, self.P2_1_3)

        if sheet is None:
            return

        start = sheet.col_values(0).index('Программы бакалавриата - всего')
        end = sheet.col_values(0).index('Всего по программам бакалавриата, специалитета и магистратуры (сумма строк '
                                        '01, 02, 03)')

        for row_num in range(start, end + 1):
            row = sheet.row_values(row_num)

            table_row = TableRowP213(row[0], row[3], row[4], row[8], row[9], row[15], row[16])

            json_text = json.dumps(table_row, ensure_ascii=False, default=my_default)
            print(json_text)

    def parse_p2_12(self, xls_path):

        book = xlrd.open_workbook(xls_path)

        book_sh_names = [name for name in book.sheet_names() if self.P2_12 in name]

        if len(book_sh_names) == 0:
            return

        for sheet_name in book_sh_names:
            sheet = book.sheet_by_name(sheet_name)

            start = sheet.col_values(0).index('Студенты, обучающиеся на условиях общего приема\r\n- всего (сумма '
                                              'строк 02, 03, 04)')
            end = sheet.col_values(0).index('лица без гражданства')

            for row_num in range(start, end + 1):
                row = sheet.row_values(row_num)

                table_row = TableRowP212(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                         row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17])

                json_text = json.dumps(table_row, ensure_ascii=False, default=my_default)
                print(json_text)
