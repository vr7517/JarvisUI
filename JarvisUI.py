# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JarvisUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Jarvis(object):
    def setupUi(self, Jarvis):
        Jarvis.setObjectName("Jarvis")
        Jarvis.resize(1227, 454)
        Jarvis.setMouseTracking(True)
        icon = QtGui.QIcon.fromTheme("OM")
        Jarvis.setWindowIcon(icon)
        Jarvis.setAutoFillBackground(False)
        Jarvis.setStyleSheet("background-color: rgb(7, 7, 7);")
        Jarvis.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(Jarvis)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1231, 471))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/cf6951100506795c4fbb8dfccc28e460.gif"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(940, 50, 111, 31))
        self.textBrowser.setStyleSheet("Background:transperent;\n"
"color: rgb(203, 115, 20);\n"
"font: 75 14pt \"digital-7\";\n"
"border:transperent;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1060, 50, 121, 31))
        self.textBrowser_2.setStyleSheet("Background:transperent;\n"
"color: rgb(203, 115, 20);\n"
"font: 75 14pt \"digital-7\";\n"
"border:transperent;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1050, 216, 81, 20))
        self.pushButton.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(203, 115, 20);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 310, 101, 20))
        self.pushButton_2.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(203, 115, 20);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-100, 10, 281, 441))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../thor.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        Jarvis.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Jarvis)
        self.statusbar.setObjectName("statusbar")
        Jarvis.setStatusBar(self.statusbar)

        self.retranslateUi(Jarvis)
        QtCore.QMetaObject.connectSlotsByName(Jarvis)

    def retranslateUi(self, Jarvis):
        _translate = QtCore.QCoreApplication.translate
        Jarvis.setWindowTitle(_translate("Jarvis", "JARVIS"))
        self.pushButton.setText(_translate("Jarvis", "Start"))
        self.pushButton_2.setText(_translate("Jarvis", "Terminate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Jarvis = QtWidgets.QMainWindow()
    ui = Ui_Jarvis()
    ui.setupUi(Jarvis)
    Jarvis.show()
    sys.exit(app.exec_())