# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiCardMonitor.ui'
#
# Created: Fri Nov 15 13:55:25 2013
#      by: PyQt4 UI code generator 4.10.3
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
        Dialog.resize(403, 333)
        self.cb_readers = QtGui.QComboBox(Dialog)
        self.cb_readers.setGeometry(QtCore.QRect(70, 10, 221, 22))
        self.cb_readers.setObjectName(_fromUtf8("cb_readers"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 11, 56, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.pb_connect = QtGui.QPushButton(Dialog)
        self.pb_connect.setGeometry(QtCore.QRect(300, 10, 91, 23))
        self.pb_connect.setObjectName(_fromUtf8("pb_connect"))
        self.tb_response = QtGui.QTextBrowser(Dialog)
        self.tb_response.setGeometry(QtCore.QRect(10, 210, 381, 111))
        self.tb_response.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"font: 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);"))
        self.tb_response.setObjectName(_fromUtf8("tb_response"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 170, 381, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 71, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.te_apdu = QtGui.QTextEdit(Dialog)
        self.te_apdu.setGeometry(QtCore.QRect(13, 80, 381, 91))
        self.te_apdu.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"font: 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);"))
        self.te_apdu.setObjectName(_fromUtf8("te_apdu"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 40, 381, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pb_req = QtGui.QPushButton(Dialog)
        self.pb_req.setGeometry(QtCore.QRect(300, 50, 91, 23))
        self.pb_req.setObjectName(_fromUtf8("pb_req"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "CardReader", None))
        self.label.setText(_translate("Dialog", "READER", None))
        self.pb_connect.setText(_translate("Dialog", "Connect", None))
        self.label_2.setText(_translate("Dialog", "Response", None))
        self.label_3.setText(_translate("Dialog", "APDU", None))
        self.pb_req.setText(_translate("Dialog", "Request", None))

