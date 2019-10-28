
import xlrd
import pyxlsb
from enum import Enum

class readXL():

    values = []
    sheets = []
    fileType = ''
    fileLocation = ''
    workbookXLSB = pyxlsb.workbook
    workbookXLSXM = ''

    def __init__(self, fileLocation):
        self.fileLocation = fileLocation
        if "xlsb" in fileLocation:
            self.fileType = XLFileType.xlsb
        elif "xlsm" in fileLocation:
            self.fileType = XLFileType.xlsm
        elif "xlsx" in fileLocation:
            self.fileType = XLFileType.xlsx
        elif "xls" in fileLocation:
            self.fileType = XLFileType.xls
        else:
            self.fileType = None

        if self.fileType == XLFileType.xlsb:
            self.workbookXLSB = pyxlsb.open_workbook(self.fileLocation)
            self.sheets = self.workbookXLSB.sheets
        else:
            self.workbookXLSXM = xlrd.open_workbook(self.fileLocation)
            self.sheets = self.workbookXLSXM.sheet_names()

    def readData(self, sheetName):
        self.values = [None]
        sheetIndex = self.getSheetIndex(sheetName)
        if self.fileType == XLFileType.xlsb:
            worksheet = self.workbookXLSB.get_sheet(sheetIndex + 1)
            for r in worksheet.rows():
                rowValues = []
                for i in range(0, len(r)):
                    # j = str(r[i]).find("v=", 0, len(str(r[i])))
                    # k = j + 3
                    # currentValue = str(r[i])[(k):]
                    # currentValue = currentValue[:(len(currentValue) - 2)]
                    currentValue = r[i].v
                    rowValues.append(currentValue)
                self.values.append(rowValues)
        else:
            worksheet = self.workbookXLSXM.sheet_by_index(sheetIndex)
            for r in range(0, worksheet.nrows):
                rowValues = []
                for c in range(0, worksheet.ncols):
                    rowValues.append(worksheet.cell(r,c).value)
                self.values.append(rowValues)

    def getSheetIndex(self, sheetName):
        sheetIndex = 0
        for i in range(0, len(self.sheets)):
            if self.sheets[i] != sheetName:
                sheetIndex = sheetIndex + 1
            else:
                return sheetIndex
        return 0


class XLFileType(Enum):
    xlsx = 1
    xlsm = 2
    xlsb = 3
    xls = 4