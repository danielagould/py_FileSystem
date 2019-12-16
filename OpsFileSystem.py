# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gouldd2\Desktop\UI Testing\mainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import FileEnums
from FileProcessor import  fileProcessor

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 644)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fileLocationBox = QtWidgets.QLineEdit(self.centralwidget)
        self.fileLocationBox.setGeometry(QtCore.QRect(100, 50, 571, 20))
        self.fileLocationBox.setObjectName("fileLocationBox")
        self.fileNameBox = QtWidgets.QLineEdit(self.centralwidget)
        self.fileNameBox.setGeometry(QtCore.QRect(100, 110, 331, 20))
        self.fileNameBox.setObjectName("fileNameBox")
        self.fileTypeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.fileTypeComboBox.setGeometry(QtCore.QRect(100, 170, 221, 22))
        self.fileTypeComboBox.setObjectName("fileTypeComboBox")
        self.currentYearBox = QtWidgets.QLineEdit(self.centralwidget)
        self.currentYearBox.setGeometry(QtCore.QRect(100, 240, 113, 20))
        self.currentYearBox.setObjectName("currentYearBox")
        self.runProcessorButton = QtWidgets.QPushButton(self.centralwidget)
        self.runProcessorButton.setGeometry(QtCore.QRect(100, 300, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.runProcessorButton.setFont(font)
        self.runProcessorButton.setObjectName("runProcessorButton")
        self.fileLocationBox_Title = QtWidgets.QLabel(self.centralwidget)
        self.fileLocationBox_Title.setGeometry(QtCore.QRect(100, 30, 81, 16))
        self.fileLocationBox_Title.setObjectName("fileLocationBox_Title")
        self.fileNameBox_Title = QtWidgets.QLabel(self.centralwidget)
        self.fileNameBox_Title.setGeometry(QtCore.QRect(100, 90, 81, 16))
        self.fileNameBox_Title.setObjectName("fileNameBox_Title")
        self.currentYearBox_Title = QtWidgets.QLabel(self.centralwidget)
        self.currentYearBox_Title.setGeometry(QtCore.QRect(100, 220, 81, 16))
        self.currentYearBox_Title.setObjectName("currentYearBox_Title")
        self.fileTypeBox_Title = QtWidgets.QLabel(self.centralwidget)
        self.fileTypeBox_Title.setGeometry(QtCore.QRect(100, 150, 81, 16))
        self.fileTypeBox_Title.setObjectName("fileTypeBox_Title")
        self.currentYearBox_Title_2 = QtWidgets.QLabel(self.centralwidget)
        self.currentYearBox_Title_2.setGeometry(QtCore.QRect(240, 220, 521, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.currentYearBox_Title_2.setFont(font)
        self.currentYearBox_Title_2.setObjectName("currentYearBox_Title_2")
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressLabel.setGeometry(QtCore.QRect(110, 420, 511, 91))
        self.progressLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.progressLabel.setObjectName("progressLabel")
        self.progressLabel_Title = QtWidgets.QLabel(self.centralwidget)
        self.progressLabel_Title.setGeometry(QtCore.QRect(110, 400, 181, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.progressLabel_Title.setFont(font)
        self.progressLabel_Title.setObjectName("progressLabel_Title")
        self.ParamTargetBox = QtWidgets.QLineEdit(self.centralwidget)
        self.ParamTargetBox.setGeometry(QtCore.QRect(100, 560, 561, 20))
        self.ParamTargetBox.setObjectName("ParamTargetBox")
        self.ParamTargetBox_Title = QtWidgets.QLabel(self.centralwidget)
        self.ParamTargetBox_Title.setGeometry(QtCore.QRect(100, 540, 81, 16))
        self.ParamTargetBox_Title.setObjectName("ParamTargetBox_Title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.fileTypeComboBox.addItems(FileEnums.fileTypeList)
        self.runProcessorButton.clicked.connect(self.setVariables)
        # self.runProcessorButton.clicked.connect(self.updateTitle)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Operations Finance SQL Insertion Tool"))
        self.runProcessorButton.setText(_translate("MainWindow", "Run File Processor"))
        self.fileLocationBox_Title.setText(_translate("MainWindow", "File Location"))
        self.fileNameBox_Title.setText(_translate("MainWindow", "File Name"))
        self.currentYearBox_Title.setText(_translate("MainWindow", "Current Year*"))
        self.fileTypeBox_Title.setText(_translate("MainWindow", "File Type"))
        self.currentYearBox_Title_2.setText(_translate("MainWindow", "Current year only necessary for SAP 9000 and T110. Otherwise leave blank"))
        self.progressLabel.setText(_translate("MainWindow", "Ready"))
        self.progressLabel_Title.setText(_translate("MainWindow", "Status:"))
        self.ParamTargetBox.setText(_translate("MainWindow", r"\\spw944efs01.euc.cpggpc.ca\B101956\MonthEnd\Operations Data Repository\Live\Data\Depot Dashboard\Parameter.json"))
        self.ParamTargetBox_Title.setText(_translate("MainWindow", "File Type"))

    def updateTitle(self):
        self.progressLabel.setText("hello")

    def setVariables(self):
        fileLocation = self.fileLocationBox.text()
        fileLocation = 'M:\\APP ZONE\\Direct Labour Model Sandbox\\p07\\MOPS\\Month End Process\\Source\\Others' # testing
        fileName = self.fileNameBox.text()
        fileName = 'R3HIER E.xls'
        currentYear = self.currentYearBox.text()
        paramFile = self.ParamTargetBox.text()
        fileType = FileEnums.fileType_dictionary[self.fileTypeComboBox.currentText()]
        fileType = FileEnums.fileType.DLM_Hierarchy_Eng # testing
        if (len(fileLocation) > 0) or (len(fileName) > 0):
            try:
                FileProcessor = fileProcessor(fileLocation, fileName, fileType, currentYear)
                f = open("Output//LogFile.txt", "r")
                contents = f.read()
                self.progressLabel.setText(fileName + ' output file created\n' + contents)
                del FileProcessor
            except Exception as e:
                self.progressLabel.setText('FAILED: ' + str(e))
                print(str(e))
        else:
            self.progressLabel.setText('ERROR: Please enter a File Name and/or File Location')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

