# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'potato2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PotatoSugarCount(object):
    def setupUi(self, PotatoSugarCount):
        PotatoSugarCount.setObjectName("PotatoSugarCount")
        PotatoSugarCount.resize(486, 203)
        self.centralwidget = QtWidgets.QWidget(PotatoSugarCount)
        self.centralwidget.setObjectName("centralwidget")
        self.Count_button = QtWidgets.QPushButton(self.centralwidget)
        self.Count_button.setGeometry(QtCore.QRect(340, 40, 131, 31))
        self.Count_button.setStyleSheet("CountButton {\n"
"    font-sizze: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"}\n"
"\n"
"CountButton:hover {\n"
"    border:bold\n"
"}\n"
"\n"
"CountButton:pressed {\n"
"    font-color: white;\n"
"    background-color: green;\n"
"}")
        self.Count_button.setObjectName("Count_button")
        self.Line_potato_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Line_potato_input.setGeometry(QtCore.QRect(340, 10, 131, 21))
        self.Line_potato_input.setClearButtonEnabled(False)
        self.Line_potato_input.setObjectName("Line_potato_input")
        self.Label_input = QtWidgets.QLabel(self.centralwidget)
        self.Label_input.setGeometry(QtCore.QRect(20, 10, 281, 21))
        self.Label_input.setObjectName("Label_input")
        self.Label_result = QtWidgets.QLabel(self.centralwidget)
        self.Label_result.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.Label_result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Label_result.setObjectName("Label_result")
        self.LabelResult1 = QtWidgets.QLabel(self.centralwidget)
        self.LabelResult1.setGeometry(QtCore.QRect(20, 110, 131, 16))
        self.LabelResult1.setObjectName("LabelResult1")
        self.LabelResult2 = QtWidgets.QLabel(self.centralwidget)
        self.LabelResult2.setGeometry(QtCore.QRect(20, 140, 131, 16))
        self.LabelResult2.setObjectName("LabelResult2")
        self.LabelResult3 = QtWidgets.QLabel(self.centralwidget)
        self.LabelResult3.setGeometry(QtCore.QRect(20, 170, 131, 16))
        self.LabelResult3.setObjectName("LabelResult3")
        self.Result1 = QtWidgets.QLabel(self.centralwidget)
        self.Result1.setGeometry(QtCore.QRect(200, 110, 271, 16))
        self.Result1.setText("")
        self.Result1.setObjectName("Result1")
        self.Result2 = QtWidgets.QLabel(self.centralwidget)
        self.Result2.setGeometry(QtCore.QRect(200, 140, 271, 16))
        self.Result2.setText("")
        self.Result2.setObjectName("Result2")
        self.Result3 = QtWidgets.QLabel(self.centralwidget)
        self.Result3.setGeometry(QtCore.QRect(200, 170, 271, 16))
        self.Result3.setText("")
        self.Result3.setObjectName("Result3")
        PotatoSugarCount.setCentralWidget(self.centralwidget)

        self.retranslateUi(PotatoSugarCount)
        QtCore.QMetaObject.connectSlotsByName(PotatoSugarCount)

    def retranslateUi(self, PotatoSugarCount):
        _translate = QtCore.QCoreApplication.translate
        PotatoSugarCount.setWindowTitle(_translate("PotatoSugarCount", "PotatoSugarCount"))
        self.Count_button.setText(_translate("PotatoSugarCount", "Рассчитать"))
        self.Label_input.setText(_translate("PotatoSugarCount", "Введите количество картошки в граммах:"))
        self.Label_result.setText(_translate("PotatoSugarCount", "Результат:"))
        self.LabelResult1.setText(_translate("PotatoSugarCount", "Содержание сахара (гр):"))
        self.LabelResult2.setText(_translate("PotatoSugarCount", "Объем сахара (мл):"))
        self.LabelResult3.setText(_translate("PotatoSugarCount", "Чайных ложек сахара:"))
