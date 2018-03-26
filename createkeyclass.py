# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createkeyclass.ui'
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
        MainWindow.setObjectName(_fromUtf8("Create Private Key"))
        MainWindow.resize(571, 128)
        MainWindow.setMinimumSize(QtCore.QSize(571, 128))
        MainWindow.setMaximumSize(QtCore.QSize(571, 128))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 59, 14))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.passtxt = QtGui.QLineEdit(self.centralwidget)
        self.passtxt.setGeometry(QtCore.QRect(90, 50, 271, 22))
        self.passtxt.setEchoMode(QtGui.QLineEdit.Password)
        self.passtxt.setObjectName(_fromUtf8("passtxt"))
        self.emailtxt = QtGui.QLineEdit(self.centralwidget)
        self.emailtxt.setGeometry(QtCore.QRect(90, 10, 271, 22))
        self.emailtxt.setObjectName(_fromUtf8("emailtxt"))
        self.okbtn = QtGui.QPushButton(self.centralwidget)
        self.okbtn.setGeometry(QtCore.QRect(420, 10, 80, 22))
        self.okbtn.setObjectName(_fromUtf8("okbtn"))
        self.genprog = QtGui.QProgressBar(self.centralwidget)
        self.genprog.setGeometry(QtCore.QRect(400, 40, 118, 23))
        self.genprog.setMaximum(1)
        self.genprog.setProperty("value", 0)
        self.genprog.setAlignment(QtCore.Qt.AlignCenter)
        self.genprog.setObjectName(_fromUtf8("genprog"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 571, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Email", None))
        self.label_2.setText(_translate("MainWindow", "Passphrase", None))
        self.okbtn.setText(_translate("MainWindow", "Create", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

