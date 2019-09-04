# Variables
####
COURSE = "3"
FILE_NAME = 'test.xlsx'
####
from openpyxl import load_workbook
from openpyxl import Workbook
import json_parser
def get_wb(filename):
    return load_workbook(filename = filename)

def get_sheets(wb):
    return [sheet for sheet in wb.sheetnames if COURSE in sheet]

def read_sheet(wb, sheetname):
    ws = wb[sheetname]
    cells = []
    for i in range(4, 49):
        cells.append(ws["B"+i.__str__()].value)
    print(json_parser.toJson(cells))
    

def main():
    wb = get_wb(FILE_NAME)
    sheets = get_sheets(wb)
    print(sheets[0])
    read_sheet(wb, sheets[0])

if __name__ == '__main__':
    main()

class Lesson:
    def __init__(self, name, ord, date):
        self.name = name
        self.ord = ord
        self.date = date
    def __init__(self, name, meta):
        self.name = name
        self.meta = meta