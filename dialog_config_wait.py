# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_config_wait.ui'
#
# Created: Tue Oct 22 08:32:56 2013
#      by: PyQt4 UI code generator 4.10.1
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(389, 200)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 59, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 40, 21, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit_2 = QtGui.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 70, 201, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(110, 30, 201, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "Puerto:", None))
        self.label.setText(_translate("Dialog", "Ip:", None))


class Inter():
    def __init__(self):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
"""
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
"""

