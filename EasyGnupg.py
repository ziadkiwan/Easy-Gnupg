from skimage.viewer.qt.QtCore import Qt
import operator
import datetime
from PyQt4.QtCore import QAbstractTableModel, SIGNAL
import mainwindow as maingui
import gnupg
import os
import createkeyclass as crkey
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox
import threading

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

windows = []


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header
    def rowCount(self, parent):
        return len(self.mylist)
    def columnCount(self, parent):
        if self.mylist:
            return len(self.mylist[0])
        else:
            return 0
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None
    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
            key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))


class crkeyExt (crkey.Ui_MainWindow):
    def __init__(self,winObj):
        self.winObj=winObj
        self.setupUi(self.winObj)
        self.winObj.show()
        self.okbtn.clicked.connect(self.addPkey)
    def addPkey(self):
        if not self.emailtxt.text().isEmpty() and not self.passtxt.text().isEmpty():
            generate = QtGui.QMessageBox()
            generate.setText("Generating Key, it might take some time Please wait!")
            generate.setWindowTitle("Generating Key")
            generate.exec_()
            self.genprog.setRange(0,0)
            work = Worker(progbar=self.genprog,email=self.emailtxt.text(),passphrase = self.passtxt.text())
        #    thread = QtCore.QThread()
        #    work.moveToThread(thread)
            #work.threads.connect(gentable(self))
            #work.completed.connect(gentable(self))
            #self.connect(work,work.signal,gentable(self))
            #self.completed.connect(gentable(self))
        #    self.connect(self.get_thread, SIGNAL("finished()"), gentable(self))
           # work.finished.connect(gentable(self))
            QtCore.QObject.connect(work, QtCore.SIGNAL("hello"), gentable)
            work.start()
        #    work.loop()
           # threading.Thread(target=generatekey(self.emailtxt.text(),self.passtxt.text())).start()
        else:
            dial = QtGui.QMessageBox()
            dial.setText(u"Please Fill all the Fields!")
            dial.setWindowTitle("Empty Fields!")
            dial.exec_()
            #dial.addButton('Okay', QtGui.QMessageBox.RejectRole)

class Worker(QtCore.QThread):
    email = "";
    passphrase = "";
    global progbar
    def __init__(self, parent=None, *args,**kwargs):
        QtCore.QThread.__init__(self,parent)
        #self.signal = QtCore.SIGNAL("signal")
        self.Init(*args,**kwargs)
    def Init(self,progbar,email,passphrase):
        self.email = email
        self.passphrase = passphrase
        self.progbar = progbar

    def run(self):
        home = os.path.expanduser("~")
        try:
			gpg = gnupg.GPG(gnupghome=home+'/gsenc')
        except TypeError:
			gpg = gnupg.GPG(homedir=home+'/gsenc')
        input_data = gpg.gen_key_input(name_email=self.email,passphrase=self.passphrase)
     #   popupmessageloading("Generating Private Key Please Wait.")
        key = gpg.gen_key(input_data)
        #print key
        self.progbar.setRange(0,1)
        self.emit(QtCore.SIGNAL("hello"), "hi from thread")
        #self.completed.emit("hello")
        #gentable(self)

class encWorker(QtCore.QThread):
    file = "";
    email = "";
    global progbar
    def __init__(self, parent=None, *args,**kwargs):
        QtCore.QThread.__init__(self,parent)
        #self.signal = QtCore.SIGNAL("signal")
        self.Init(*args,**kwargs)
    def Init(self,progbar,file,email):
        self.file = file
        self.email = email
        self.progbar = progbar

    def run(self):
        home = os.path.expanduser("~")
        try:
			gpg = gnupg.GPG(gnupghome=home+'/gsenc')
        except TypeError:
			gpg = gnupg.GPG(homedir=home+'/gsenc')
     #  input_data = gpg.gen_key_input(name_email=self.email,passphrase=self.passphrase)
     #   popupmessageloading("Generating Private Key Please Wait.")
        usesless = str(self.file)
        location = usesless+'.gpg'
        with open(usesless, 'rb') as f:
            status = gpg.encrypt_file(
                f, recipients=[str(self.email)],
                output=location,always_trust=True)
        #print key
        self.progbar.setRange(0,1)
        self.emit(QtCore.SIGNAL("status"), status.stderr)
        global encresut
        encresut = status.stderr
        #self.completed.emit("hello")
        #gentable(self)

class decworker(QtCore.QThread):
    file = "";
    passphrase = "";
    global progbar
    def __init__(self, parent=None, *args,**kwargs):
        QtCore.QThread.__init__(self,parent)
        #self.signal = QtCore.SIGNAL("signal")
        self.Init(*args,**kwargs)
    def Init(self,progbar,file,passphrase):
        self.file = file
        self.passphrase = passphrase
        self.progbar = progbar

    def run(self):
        home = os.path.expanduser("~")
        try:
			gpg = gnupg.GPG(gnupghome=home+'/gsenc')
        except TypeError:
			gpg = gnupg.GPG(homedir=home+'/gsenc')
    #    print self.file
        usesless = str(self.file)
        location = usesless[:len(usesless)-4]
        with open(usesless, 'rb') as f:
            status = gpg.decrypt_file(
                f, passphrase=self.passphrase,
                output=location)
        #print key
        self.progbar.setRange(0,1)
      #  print status.stderr
        self.emit(QtCore.SIGNAL("decstatus"), status.stderr)
        global encresut
        encresut = status.stderr
        #self.completed.emit("hello")
        #gentable(self)

Headers = ["Type","Key ID","Length","Date","Email","Fingerprint"]
global keytable
encresut = ""
class extendmain (maingui.Ui_MainWindow):
    def __init__(self,windowObj):
        self.windowObj=windowObj
        self.setupUi(self.windowObj)
        self.windowObj.show()
        self.createkey.clicked.connect(self.showCrkey)
        self.importkey.clicked.connect(self.showimportdialog)
        self.browsefile.clicked.connect(self.showfiledialog)
        self.dec.clicked.connect(self.decrypytfile)
        self.enc.clicked.connect(self.encryptfile)
        global keytable
        keytable = self.keys
     #   self.windowObj.connect(keytable, SIGNAL('customContextMenuRequested(const QPoint &)'), self.contextMenuEvent)
        keytable.setContextMenuPolicy(Qt.CustomContextMenu)
        gentable()
        keytable.customContextMenuRequested.connect(self.contextMenuEvent)
        windows.append(self)
    def contextMenuEvent(self):
        menu = QtGui.QMenu(self.windowObj)
        Exportaction = QtGui.QAction("Export Key",self.windowObj)
        Exportaction.triggered.connect(lambda: self.exportkey())
        Deletekey = QtGui.QAction("Delete Key",self.windowObj)
        Deletekey.triggered.connect(lambda: self.deletekey())
        menu.addAction(Exportaction)
        menu.addAction(Deletekey)
        menu.popup(QtGui.QCursor.pos())
        #action = menu.exec_(keytable.mapToGlobal(position))
        #menu.popup(QtGui.QCursor.pos())
    def deletekey(self):
        for i in self.keys.selectionModel().selection().indexes():
            row, column = i.row(), i.column()
        fingerprints = self.keys.model().index(row,5).data().toPyObject()
        keytype = self.keys.model().index(row,0).data().toPyObject()
        keytypebool = True
        home = os.path.expanduser("~")
        try:
			gpg1 = gnupg.GPG(gnupghome=home+'/gsenc')
        except TypeError:
			gpg1 = gnupg.GPG(homedir=home+'/gsenc')
        if "pub" in keytype:
            keytypebool = False
            privatelist = gpg1.list_keys(secret=True)
            for pkeyin in privatelist:
                if fingerprints in pkeyin.get("fingerprint"):
                    dial = QtGui.QMessageBox()
                    dial.setText(u"The private key exists, please delete the private key first!")
                    dial.setWindowTitle("Missing Public Key!")
                    dial.exec_()
                    return
        gpg1.delete_keys(fingerprints=str(fingerprints),secret=keytypebool)
        gentable()
    def exportkey(self):
        for i in self.keys.selectionModel().selection().indexes():
            row, column = i.row(), i.column()
        fingerprint = self.keys.model().index(row,5).data().toPyObject()
        keytype = self.keys.model().index(row,0).data().toPyObject()
        home = os.path.expanduser("~")
        try:
			gpg1 = gnupg.GPG(gnupghome=home+'/gsenc')
        except TypeError:
			gpg1 = gnupg.GPG(homedir=home+'/gsenc')
        allkeystemp = []
        private = False;
        if "sec" in keytype:
            private = True;
            allkeystemp = gpg1.list_keys(True)
        else:
            allkeystemp = gpg1.list_keys()
        keytoexport = None
        for key in allkeystemp:
            if fingerprint in key.get("fingerprint"):
                if(private):
                    keytoexport = gpg1.export_keys(key.get("keyid"), True)
                else:
                    keytoexport = gpg1.export_keys(key.get("keyid"))
                filename = QtGui.QFileDialog.getSaveFileName(self.windowObj,"Export Key To", ".asc","")
                if filename:
                    with open(filename, 'w') as f:
                        f.write(keytoexport)
        #    data = i.data()
        #print data.toPyObject()
    def encryptfile(self):
        try:
            for i in self.keys.selectionModel().selection().indexes():
                row, column = i.row(), i.column()
            keytype = self.keys.model().index(row,0).data().toPyObject()
            encemail = self.keys.model().index(row,4).data().toPyObject()
            if "pub" not in keytype:
                dial = QtGui.QMessageBox()
                dial.setText(u"Please select a public key from the table then press encrypt")
                dial.setWindowTitle("Missing Public Key!")
                dial.exec_()
                return
        except:
            dial = QtGui.QMessageBox()
            dial.setText(u"Please select a public key from the table then press encrypt")
            dial.setWindowTitle("Missing Public Key!")
            dial.exec_()
            return
        if not self.lineEdit.text().isEmpty():
            generate = QtGui.QMessageBox()
            generate.setText(u"Encrypting the File, it might take some time Please wait!")
            generate.setWindowTitle("Encrypting File")
            generate.exec_()
            self.cryptoprog.setRange(0,0)
            work = encWorker(progbar=self.cryptoprog,file=self.lineEdit.text(),email = encemail)
            QtCore.QObject.connect(work, QtCore.SIGNAL("status"), self.showencresult)
            work.start()
        else:
            dial = QtGui.QMessageBox()
            dial.setText(u"Please Choose a file")
            dial.setWindowTitle("Empty Fields!")
            dial.exec_()
    def decrypytfile(self):
        # try:
        #     for i in self.keys.selectionModel().selection().indexes():
        #         row, column = i.row(), i.column()
        #     keytype = self.keys.model().index(row,0).data().toPyObject()
        #     encemail = self.keys.model().index(row,4).data().toPyObject()
        #     if "sec" not in keytype:
        #         dial = QtGui.QMessageBox()
        #         dial.setText(u"Please select a private key from the table then press encrypt")
        #         dial.setWindowTitle("Missing Public Key!")
        #         dial.exec_()
        #         return
        # except:
        #     dial = QtGui.QMessageBox()
        #     dial.setText(u"Please select a private key from the table then press encrypt")
        #     dial.setWindowTitle("Missing Public Key!")
        #     dial.exec_()
        #     return
        if not self.lineEdit.text().isEmpty():
            # generate = QtGui.QMessageBox()
            # generate.setText(u"Decrypting the File, it might take some time Please wait!")
            # generate.setWindowTitle("Decrypting File")
            # generate.exec_()
            input = QtGui.QInputDialog
            result = input.getText(self.windowObj, 'Decryption Passphrase', 'Please enter the decryption passphrase:')
            if(result[1]):
            #if ok:
                self.cryptoprog.setRange(0,0)
                self.work = decworker(progbar=self.cryptoprog,file=self.lineEdit.text(),passphrase = str(result[0]))
                QtCore.QObject.connect(self.work, QtCore.SIGNAL("decstatus"), self.showencresult)
                self.work.start()
        else:
            dial = QtGui.QMessageBox()
            dial.setText(u"Please Choose a file")
            dial.setWindowTitle("Empty Fields!")
            dial.exec_()
    def showencresult(self):
        self.cryptoprog.setRange(0,1)
        generate = QtGui.QMessageBox()
        generate.setText(encresut+u"")
        generate.setWindowTitle("Result")
        generate.exec_()

    def showCrkey(self):
        crkeyWin=QtGui.QMainWindow()
        crkeyUI=crkeyExt(crkeyWin)
        windows.append(crkeyUI)
       # crkeyWin.show()
    def showimportdialog(self):
        importkey = str(QtGui.QFileDialog.getOpenFileName(self.windowObj, "Select the Key",""))
        if importkey:
            home = os.path.expanduser("~")
            try:
				gpg = gnupg.GPG(gnupghome=home+'/gsenc')
            except TypeError:
				gpg = gnupg.GPG(homedir=home+'/gsenc')
            key_data = open(importkey).read()
            import_result = gpg.import_keys(key_data)
            gentable()
    def showfiledialog(self):
        filetop = str(QtGui.QFileDialog.getOpenFileName(self.windowObj, "Select the file",""))
        self.lineEdit.setText(filetop)

allkeys = [];
def gentable():
        global allkeys
        allkeys = []
        home = os.path.expanduser("~")
        try:
			gpg = gnupg.GPG(gnupghome=home+'/gsenc')
        except TypeError:
			gpg = gnupg.GPG(homedir=home+'/gsenc')
        public_keys = gpg.list_keys()
        private_keys = gpg.list_keys(True)
        for key in private_keys:
            temp = []
            temp.append(key.get("type"))
            temp.append(key.get("keyid"))
            temp.append(key.get("length"))
            temp.append(datetime.datetime.fromtimestamp(int(key.get("date"))).strftime('%Y-%m-%d %H:%M:%S'))
            temp.append(key.get("uids")[0][key.get("uids")[0].find('<')+1:key.get("uids")[0].find('>')])
            temp.append(key.get("fingerprint"))
            allkeys.append(temp)
        for key in public_keys:
            temp = []
            temp.append(key.get("type"))
            temp.append(key.get("keyid"))
            temp.append(key.get("length"))
            temp.append(datetime.datetime.fromtimestamp(int(key.get("date"))).strftime('%Y-%m-%d %H:%M:%S'))
            temp.append(key.get("uids")[0][key.get("uids")[0].find('<')+1:key.get("uids")[0].find('>')])
            temp.append(key.get("fingerprint"))
            allkeys.append(temp)
        table_model = MyTableModel(myapp ,allkeys, Headers)
        keytable.setModel(table_model)
        keytable.resizeColumnsToContents()
        keytable.setSortingEnabled(True)
if __name__ == "__main__":
    import sys
    myapp=QtGui.QApplication(sys.argv)
    MainWIndow=QtGui.QMainWindow()
    ui=extendmain(MainWIndow)
    # crMainWindow=QtGui.QMainWindow()
    # crKeys=crkeyExt(crMainWindow)
    # app = QtGui.QApplication(sys.argv)
    # MainWindow = QtGui.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(myapp.exec_())

