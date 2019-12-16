from datetime import datetime
import numpy as np


class dataFilter:

    def __init__(self, inputValues, inputStartRow):
        self.values = inputValues
        self.startRow = inputStartRow

    def deleteValues(self):
        self.values.clear()

    def filter95xx(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                for k in range(0, 10):
                    if "#" in str(currentRow[k]) and k == 4:
                        currentRowNew.append(None)
                    else:
                        currentRowNew.append(currentRow[k])
                currentRowNew.append(self.correctNegative(self.removeComma(currentRow[10])))
                newValues.append(currentRowNew)
        return newValues

    def filter95xxWKLY(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                for k in range(0, 11):
                    if "#" in str(currentRow[k]) and k == 4:
                        currentRowNew.append(None)
                    else:
                        currentRowNew.append(currentRow[k])
                currentRowNew.append(self.correctNegative(self.removeComma(currentRow[11])))
                newValues.append(currentRowNew)
        return newValues

    def filter95xxWKLY_Custom(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                for k in range(0, 11):
                    if "#" in str(currentRow[k]) and k == 4:
                        currentRowNew.append(None)
                    else:
                        if k == 10:
                            currentRowNew.append(self.convertToInt(currentRow[k][-2:]))
                        else:
                            currentRowNew.append(currentRow[k])
                currentRowNew.append(self.correctNegative(self.removeComma(currentRow[11])))
                newValues.append(currentRowNew)
        return newValues

    def filterHHBonus(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 1:
                currentRowNew.append(self.convertToInt(self.removeSpaces(currentRow[1])))   # FiscalYear
                currentRowNew.append(self.convertToInt(self.removeSpaces(currentRow[2])))   # FPeriod
                currentRowNew.append(self.convertToInt(self.removeSpaces(currentRow[3])))   # ActType
                currentRowNew.append(self.convertToInt(self.removeSpaces(currentRow[4])))   # CostElement
                currentRowNew.append(self.removeSpaces(currentRow[5]))  # CostElementName
                currentRowNew.append(self.convertToInt(self.removeSpaces(currentRow[6])))   # CC
                CCName_ActType = self.removeSpaces(currentRow[7])   # Extra the CCName/ActTypeName hybrid
                slashLocation = str(CCName_ActType).find('/')   # Find location of slash
                length = len(str(CCName_ActType))   # Find full length of CCName_ActType
                # Set CCName to the length before slash and remove spaces
                CCName = self.removeSpaces(str(CCName_ActType)[:(slashLocation)])
                # Set ActType to the length after slash and remove spaces
                ActType = self.removeSpaces(str(CCName_ActType)[-(length - slashLocation - 1):])
                currentRowNew.append(CCName)    # Append CCName
                currentRowNew.append(ActType)   # Append ActType
                # Remove the spaces, commas and correct the negative (minus sign after the number)
                # and convert to Float
                # Val
                currentRowNew.append(self.convertToFloat(
                    self.correctNegative_HHBonus(self.removeComma(self.removeSpaces(currentRow[8])))))
                # Remove the spaces, commas and correct the negative (minus sign after the number)
                # and convert to Float
                # Qty
                currentRowNew.append(self.convertToFloat(
                    self.correctNegative_HHBonus(self.removeComma(self.removeSpaces(currentRow[9])))))
                newValues.append(currentRowNew)
        return newValues

    def filter9000(self, fiscalYear):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                currentRowNew.append(currentRow[0])
                currentRowNew.append(currentRow[1])
                currentRowNew.append(currentRow[2])
                if '#' in str(currentRow[3]):
                    currentRowNew.append(None)
                else:
                    currentRowNew.append(self.convertToInt(currentRow[3]))
                currentRowNew.append(currentRow[4])
                if '#' in str(currentRow[5]):
                    currentRowNew.append(None)
                else:
                    currentRowNew.append(self.convertToInt(currentRow[5]))
                currentRowNew.append(currentRow[6])
                currentRowNew.append(int(fiscalYear))
                currentRowNew.append(self.convertToInt(currentRow[7]))
                currentRowNew.append(self.convertToFloat(self.correctNegative(self.removeComma(currentRow[8]))))
                currentRowNew.append(self.convertToFloat(self.correctNegative(self.removeComma(currentRow[9]))))
                currentRowNew.append(self.convertToFloat(self.correctNegative(self.removeComma(currentRow[10]))))
                newValues.append(currentRowNew)
        return newValues

    def filter9000_DLM(self, fiscalYear):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                currentRowNew.append(currentRow[0])
                currentRowNew.append(currentRow[1])
                if '#' in str(currentRow[2]):
                    currentRowNew.append(None)
                else:
                    currentRowNew.append(self.convertToInt(currentRow[2]))
                currentRowNew.append(currentRow[3])
                if '#' in str(currentRow[4]):
                    currentRowNew.append(None)
                else:
                    currentRowNew.append(self.convertToInt(currentRow[4]))
                currentRowNew.append(currentRow[5])
                currentRowNew.append(int(fiscalYear))
                currentRowNew.append(self.convertToInt(currentRow[6]))
                currentRowNew.append(self.convertToFloat(self.correctNegative(self.removeComma(currentRow[7]))))
                currentRowNew.append(self.convertToFloat(self.correctNegative(self.removeComma(currentRow[8]))))
                currentRowNew.append(self.convertToFloat(self.correctNegative(self.removeComma(currentRow[9]))))
                newValues.append(currentRowNew)
        return newValues

    def filter95xxYOYAdj(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                for k in range(1, 4):
                    currentRowNew.append(currentRow[k])
                if "#" in str(currentRow[4]):
                    currentRowNew.append(None)
                else:
                    currentRowNew.append(currentRow[4])
                for k in range(5,9):
                    currentRowNew.append(currentRow[k])
                currentRowNew.append(self.fiscalYear)
                for k in range(9,14):
                    currentRow[k] = self.removeComma(currentRow[k])
                    currentRowNew.append(self.convertToFloat(self.correctNegative(currentRow[k])))
                newValues.append(currentRowNew)
        return newValues

    def filterYOYAdj(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                currentRowNew.append(int(currentRow[0]))
                currentRowNew.append(currentRow[2])
                currentRowNew.append(currentRow[3])
                currentRowNew.append(int(currentRow[4]))
                for j in range(5, 17):
                    currentRowNew.append(self.convertToFloat(currentRow[j]))
                newValues.append(currentRowNew)
        return newValues

    def filterFieldRollup(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                GM = str(currentRow[2][:9])
                if GM in self.FieldRollupGMs:
                    currentRowNew.append(self.convertToInt(currentRow[0]))
                    currentRowNew.append(currentRow[1])
                    currentRowNew.append(str(currentRow[2][:9]))
                    currentRowNew.append(str(currentRow[2]))
                    currentRowNew.append(str(currentRow[3][:9]))
                    currentRowNew.append(str(currentRow[3]))
                    currentRowNew.append(str(currentRow[4][:9]))
                    currentRowNew.append(str(currentRow[4]))
                    currentRowNew.append(str(currentRow[5]))
                    if currentRow[8] == 'Non-Plant':
                        currentRowNew.append(None)
                        currentRowNew.append(0)
                    else:
                        currentRowNew.append(str(currentRow[8]))
                        currentRowNew.append(1)
                    if currentRow[10] == 'Non-Hub':
                        currentRowNew.append(0)
                    else:
                        currentRowNew.append(1)
                    if currentRow[11] == 'Non-Depot':
                        currentRowNew.append(0)
                        currentRowNew.append(0)
                    else:
                        currentRowNew.append(1)
                        if currentRowNew[11] == 'Depot-MUC':
                            currentRowNew.append(1)
                        else:
                            currentRowNew.append(0)
                    newValues.append(currentRowNew)
        return newValues


    def filterSAPHierarchy(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                if currentRow[6][:9] == "SHN103974":
                    if type(currentRow[0]) != str:
                        currentRowNew.append(int(currentRow[0]))
                        currentRowNew.append(currentRow[1])
                        currentRowNew.append(str(currentRow[6])[:9])
                        currentRowNew.append(str(currentRow[7])[:9])
                        currentRowNew.append(str(currentRow[8])[:9])
                        currentRowNew.append(str(currentRow[9])[:9])
                        newValues.append(currentRowNew)
        return newValues

    def filterTOPRS(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                if currentRow[0] != 'None' and currentRow[0] is not None:
                    currentRowNew.append(str(currentRow[0]))
                    currentRowNew.append(str(currentRow[1]))
                    for j in range(4, 57):
                        if currentRow[j] != 'None':
                            try:
                                appendValue = float(currentRow[j])
                            except:
                                appendValue = None
                        else:
                            appendValue = None
                        currentRowNew.append(appendValue)
                    newValues.append(currentRowNew)
        return newValues

    def filterTOPRSRollup(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                currentRowNew.append(self.convertToInt(currentRow[0]))
                for j in range(1,18):
                    currentRowNew.append(self.checkNULL_str(currentRow[j]))
                newValues.append(currentRowNew)
        return newValues

    def filterLastPlanA(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                currentRowNew.append(currentRow[1])
                currentRowNew.append(self.convertToInt(currentRow[2]))
                currentRowNew.append(self.convertToInt(currentRow[3]))
                currentRowNew.append(currentRow[4])
                print(i)
                currentRowNew.append(self.convertToDate(currentRow[5]))
                currentRowNew.append(currentRow[6])
                if str(currentRow[8]).lower() == 'y':
                    currentRowNew.append('PT')
                elif str(currentRow[8]).lower() == 'n':
                    currentRowNew.append('NonPT')
                elif str(currentRow[8]).lower() == 'se':
                    currentRowNew.append('SE')
                else:
                    currentRowNew.append(None)
                newValues.append(currentRowNew)
        return newValues

    def filter1508(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                currentRowNew.append(self.convertToInt(currentRow[0]))
                for j in range(1, 7):
                    currentRowNew.append(currentRow[j])
                currentRowNew.append(self.convertToInt(currentRow[7]))
                for k in range(8, 12):
                    currentRowNew.append(currentRow[k])
                currentRowNew.append(self.convertToInt(currentRow[12]))
                for l in range(13, 66):
                    currentRowNew.append(self.convertToFloat(currentRow[l]))
                newValues.append(currentRowNew)
        return newValues

    def filterWC2CC(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                currentRowNew.append(currentRow[0])
                currentRowNew.append(currentRow[1])
                currentRowNew.append(currentRow[2])
                currentRowNew.append(currentRow[5])
                print(currentRow[6])
                currentRowNew.append(self.convertToInt(currentRow[6]))
                currentRowNew.append(currentRow[11])
                currentRowNew.append(currentRow[12])
                currentRowNew.append(currentRow[15])
                currentRowNew.append(currentRow[16])
                currentRowNew.append(currentRow[21])
                currentRowNew.append(currentRow[22])
            newValues.append(currentRowNew)
        return newValues

    def filterT110(self, valuesHours, valuesDollars, startRowHours, startRowDollars, fiscalYear):
        newValues = []
        for i in range(startRowHours, len(valuesHours)):
            currentRow = valuesHours[i]
            currentRowNew = []
            if len(currentRow) > 0 and currentRow[0] != ' ' and currentRow[1] != ' ':
                currentRowNew.append(str('Hours'))  # DataType
                currentRowNew.append(int(fiscalYear))   # Fiscal Year
                currentRowNew.append(self.convertToInt(currentRow[0]))
                if 'plant' in str(currentRow[1]).lower():
                    currentRowNew.append(int(1)) # Plant
                else:
                    currentRowNew.append(int(0)) # Non Plant
                currentRowNew.append(currentRow[2]) # Driver
                currentRowNew.append(currentRow[3]) # SubDriver
                currentRowNew.append(currentRow[5]) # Act Type
                currentRowNew.append(currentRow[6]) # GLCE Group
                currentRowNew.append(currentRow[7]) # Time Group
                valuesByPeriod = self.Weeks_To_Periods(currentRow, 11)
                for p in range(0, 12):
                    currentRowNew.append(valuesByPeriod[p])
                newValues.append(currentRowNew)
        for i in range(startRowDollars, len(valuesDollars)):
            currentRow = valuesDollars[i]
            currentRowNew = []
            if len(currentRow) > 0 and currentRow[0] != ' ' and currentRow[1] != ' ':
                currentRowNew.append(str('Dollars'))
                currentRowNew.append(int(fiscalYear))  # Fiscal Year
                currentRowNew.append(self.convertToInt(currentRow[0]))
                if 'plant' in str(currentRow[1]).lower():
                    currentRowNew.append(int(1))  # Plant
                else:
                    currentRowNew.append(int(0))  # Non Plant
                currentRowNew.append(currentRow[2]) # Driver
                currentRowNew.append(currentRow[3]) # SubDriver
                currentRowNew.append(currentRow[5]) # Act Type
                currentRowNew.append(currentRow[6]) # GLCE Group
                currentRowNew.append(currentRow[7]) # Time Group
                for p in range(13, 25):
                    currentRowNew.append(self.convertToFloat(currentRow[p]))
                newValues.append(currentRowNew)
        return newValues

    def Weeks_To_Periods(self, values, startCol):
        periodicValues = []
        periodValue = 0.0
        weeksInPeriod = np.array([[0,4],[4,8],[8,13],[13,17],[17,21],[21,26],[26,30],[30,34],[34,39],[39,43],[43,47],[47,53]])
        for p in range(0,12):
            periodStart = startCol + weeksInPeriod[p,0]
            periodEnd = startCol + weeksInPeriod[p,1]
            for i in range(periodStart, periodEnd):
                periodValue += self.convertToFloat(values[i])
            periodicValues.append(periodValue)
            periodValue = 0.0
        return periodicValues

    def filterTOPRSPlan(self):
        newValues = []
        for i in range (self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                currentRowNew.append(str(currentRow[3])[:9])
                currentRowNew.append(str(currentRow[3]))
                currentRowNew.append(str(currentRow[4])[:9])
                currentRowNew.append(str(currentRow[4]))
                currentRowNew.append(str(currentRow[5])[:9])
                currentRowNew.append(str(currentRow[5]))
                currentRowNew.append(str(currentRow[6]))
                currentRowNew.append(self.convertToInt(currentRow[0]))
                currentRowNew.append(str(currentRow[2]))
                currentRowNew.append(str(currentRow[7]))
                currentRowNew.append(self.convertToInt(currentRow[64]))
                currentRowNew.append(str(currentRow[1]))
                currentRowNew.append(str(currentRow[65]))
                if str(currentRow[67]) == 'Plant':
                    currentRowNew.append(1)
                else:
                    currentRowNew.append(0)
                currentRowNew.append(self.checkNULL_str(currentRow[68]))
                currentRowNew.append(self.checkNULL_str(currentRow[69]))
                currentRowNew.append(self.checkNULL_str(currentRow[70]))
                currentRowNew.append(self.checkNULL_str(currentRow[71]))
                currentRowNew.append(self.checkNULL_str(currentRow[72]))
                currentRowNew.append(self.checkNULL_str(currentRow[74]))
                currentRowNew.append(self.checkNULL_str(currentRow[75]))
                for j in range(11, 64):
                    currentRowNew.append(self.convertToFloat(currentRow[j]))
                newValues.append(currentRowNew)
        return newValues

    def filterRestructure(self, isActual):
        newValues = []
        for i in range (self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                if isActual:
                    currentRowNew.append('Actual')
                else:
                    currentRowNew.append('Target')
                currentRowNew.append(self.convertToInt(currentRow[0]))
                currentRowNew.append(currentRow[1])
                currentRowNew.append(currentRow[2])
                currentRowNew.append(currentRow[3])
                currentRowNew.append(self.convertToFloat(self.correctNegative(self.removeComma(currentRow[4]))))
                newValues.append(currentRowNew)
        return newValues

    def filterT313(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                currentRowNew.append(currentRow[3])
                currentRowNew.append(currentRow[2])
                currentRowNew.append(currentRow[4])
                currentRowNew.append(currentRow[5])
                currentRowNew.append(self.convertToInt(currentRow[1]))
                for j in range(6, 21):
                    currentRowNew.append(self.convertToFloat(self.correctNegative(self.removeComma(currentRow[j]))))
                newValues.append(currentRowNew)
        return newValues

    def filterT008(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                currentRowNew.append(currentRow[0])
                currentRowNew.append(currentRow[1])
                for j in range(2, 7):
                    currentRowNew.append(self.convertToFloat(self.correctNegative(self.removeComma(currentRow[j]))))
                newValues.append(currentRowNew)
        return newValues

    def filterHier(self):
        newValues = []
        for i in range(self.startRow, len(self.values)):
            currentRow = self.values[i]
            currentRowNew = []
            if len(currentRow) > 0:
                if currentRow[5][:9] == 'SHN102910':
                    if 'SHN' in str(currentRow[0]):  #CC
                        currentRowNew.append(currentRow[0][:9])
                    else:
                        currentRowNew.append(currentRow[0])
                    currentRowNew.append(currentRow[1])      # CCName
                    currentRowNew.append(currentRow[5][:9])  # SVP
                    currentRowNew.append(currentRow[6][:9])  # VP
                    currentRowNew.append(currentRow[7][:9])  # GM
                    currentRowNew.append(currentRow[8][:9])  # Dir
                    currentRowNew.append(currentRow[9][:9])  # Mgr
                    currentRowNew.append(currentRow[10][:9])  # Support
                    newValues.append(currentRowNew)
        return newValues

    def removeComma(self, currentValue):
        if ',' in str(currentValue):
            commaLocation = str(currentValue).find(',')
            length = len(str(currentValue))
            currentValue = str(currentValue)[:(commaLocation)] + str(currentValue)[
                                                                   -(length - commaLocation - 1):]
        if ',' in str(currentValue):        #This is repeated to remove multiple instances of commas (millions and billions
            commaLocation = str(currentValue).find(',')
            length = len(str(currentValue))
            currentValue = str(currentValue)[:(commaLocation)] + str(currentValue)[
                                                                   -(length - commaLocation - 1):]
        if ',' in str(currentValue):
            commaLocation = str(currentValue).find(',')
            length = len(str(currentValue))
            currentValue = str(currentValue)[:(commaLocation)] + str(currentValue)[
                                                                   -(length - commaLocation - 1):]
        return currentValue

    def correctNegative(self, currentValue):
        if str(currentValue)[:1] == "(" and currentValue is not None:
            currentValue = float(str(currentValue)[1:-1]) * -1
        return currentValue

    def correctNegative_HHBonus(self, currentValue):
        if str(currentValue)[-1:] == '-' and currentValue is not None:
            currentValue = float(str(currentValue)[:-1]) * -1
        return currentValue

    def convertToFloat(self, currentValue):
        if (currentValue == '') or (currentValue == ' ') or (currentValue is None):
            return float(0)
        else:
            return float(currentValue)

    def convertToInt(self, currentValue):
        if (currentValue == '') or (currentValue == ' ') or (currentValue is None):
            return None
        else:
            return int(currentValue)

    def convertToDate(self, currentValue):
        if (currentValue == '') or (currentValue == ' '):
            return None
        else:
            return datetime.fromordinal(int(currentValue))

    def checkNULL_str(self, currentValue):
        if (currentValue == '') or (currentValue == ' ') or (currentValue is None):
            return None
        else:
            return str(currentValue)

    def removeSpaces(self, currentValue):
        space = ' '
        if (currentValue == '') or (currentValue == ' ') or (currentValue is None):
            return None
        else:
            return space.join(currentValue.split())




