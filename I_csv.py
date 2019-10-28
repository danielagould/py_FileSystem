import csv

class readCSV():

    values = []
    fileLocation = ""

    def __init__(self,fileLocation, dialectName):
        readCSV.fileLocation = fileLocation
        csv.register_dialect("SAPoutput",delimiter=";")
        csv.register_dialect("HHBonus", delimiter="|")
        readCSV.readData(dialectName)

    @staticmethod
    def readData(dialectName):
        with open(readCSV.fileLocation) as csvFile:
            csvReader = csv.reader(csvFile,dialectName)
            for row in csvReader:
                rowValues = []
                for i in range(0,len(row)):
                    rowValues.append(row[i])
                readCSV.values.append(rowValues)

    def __delete__(self, instance):
        readCSV.values.clear()