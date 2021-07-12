# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import xlrd
import xlwt
from decimal import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #wt
    n_row = 0
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet("new sheet")
    title  = ["t01", "t02"]
    worksheet.write(0, 0, title[0])
    worksheet.write(0, 1, title[1])
    n_row += 1

    # rd
    filename = "/Users/yu/Desktop/demo/data.xls"
    data = xlrd.open_workbook(filename)
    # first sheets
    table = data.sheets()[0]

    nrows = table.nrows
    #get all 1st col
    name_list = [str(table.cell_value(i, 1)) for i in range(0, nrows)]
    s = set()
    for name in name_list:
        s.add(name)
    # print(len(s))

    for name in sorted(s, reverse=False):
        print(name)
        t_value = Decimal(0)
        for i in range(2, nrows):
            r = table.row_values(i)
            if len(r) > 1:
                if r[1] == name:
                    print(r)
                    if len(r) == 2 :
                        worksheet.write(n_row, 0, r[0])
                        worksheet.write(n_row, 1, str(r[1]))
                        n_row += 1
                        t_value += Decimal(r[5])
    # print(name_list)
    workbook.save("new.xls")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
