# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mapper_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(371, 314)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtQuery = QtWidgets.QLineEdit(self.centralwidget)
        self.txtQuery.setGeometry(QtCore.QRect(10, 30, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtQuery.setFont(font)
        self.txtQuery.setObjectName("txtQuery")
        self.btnAction = QtWidgets.QPushButton(self.centralwidget)
        self.btnAction.setGeometry(QtCore.QRect(280, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnAction.setFont(font)
        self.btnAction.setObjectName("btnAction")
        self.txtLongitude = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtLongitude.setGeometry(QtCore.QRect(10, 80, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtLongitude.setFont(font)
        self.txtLongitude.setObjectName("txtLongitude")
        self.txtLatitude = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtLatitude.setGeometry(QtCore.QRect(180, 80, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtLatitude.setFont(font)
        self.txtLatitude.setObjectName("txtLatitude")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 130, 341, 91))
        self.textEdit.setObjectName("textEdit")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(20, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.btnMap = QtWidgets.QPushButton(self.centralwidget)
        self.btnMap.setGeometry(QtCore.QRect(120, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnMap.setFont(font)
        self.btnMap.setObjectName("btnMap")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ILD-Mapper"))
        self.btnAction.setText(_translate("MainWindow", "Parse"))
        self.label.setText(_translate("MainWindow", "Query :"))
        self.label_2.setText(_translate("MainWindow", "Longitude :"))
        self.label_3.setText(_translate("MainWindow", "Latitude :"))
        self.label_4.setText(_translate("MainWindow", "Description :"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.btnMap.setText(_translate("MainWindow", "Map"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
