# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.createkey = QtGui.QPushButton(self.centralwidget)
        self.createkey.setGeometry(QtCore.QRect(0, 0, 121, 71))
        self.createkey.setObjectName(_fromUtf8("createkey"))
        self.importkey = QtGui.QPushButton(self.centralwidget)
        self.importkey.setGeometry(QtCore.QRect(120, 0, 111, 71))
        self.importkey.setObjectName(_fromUtf8("importkey"))
        self.keys = QtGui.QTableView(self.centralwidget)
        self.keys.setGeometry(QtCore.QRect(0, 100, 801, 361))
        self.keys.setObjectName(_fromUtf8("keys"))
        self.browsefile = QtGui.QPushButton(self.centralwidget)
        self.browsefile.setGeometry(QtCore.QRect(0, 490, 80, 22))
        self.browsefile.setObjectName(_fromUtf8("browsefile"))
        self.enc = QtGui.QPushButton(self.centralwidget)
        self.enc.setGeometry(QtCore.QRect(430, 490, 80, 22))
        self.enc.setObjectName(_fromUtf8("enc"))
        self.dec = QtGui.QPushButton(self.centralwidget)
        self.dec.setGeometry(QtCore.QRect(510, 490, 80, 22))
        self.dec.setObjectName(_fromUtf8("dec"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(8, 74, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.cryptoprog = QtGui.QProgressBar(self.centralwidget)
        self.cryptoprog.setGeometry(QtCore.QRect(610, 490, 118, 23))
        self.cryptoprog.setMaximum(1)
        self.cryptoprog.setProperty("value", 0)
        self.cryptoprog.setObjectName(_fromUtf8("cryptoprog"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 490, 331, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Easy Gnupg", None))
        self.createkey.setText(_translate("MainWindow", "Create Private key", None))
        self.importkey.setText(_translate("MainWindow", "Import Key", None))
        self.browsefile.setText(_translate("MainWindow", "Choose File", None))
        self.enc.setText(_translate("MainWindow", "Encrypt", None))
        self.dec.setText(_translate("MainWindow", "Decrypt", None))
        self.label.setText(_translate("MainWindow", "Available Keys:", None))

