#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HeesangLee
#
# Created:     19/08/2013
# Copyright:   (c) HeesangLee 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import (Qt, SIGNAL,QTimer)
from PyQt4.QtGui import (QApplication, QDialog, QLineEdit, QTextBrowser,
        QVBoxLayout,QPushButton,QLabel,QGraphicsScene )
from PyQt4 import QtGui

import os

import uiCardMonitor
from smartcard.System import readers
from smartcard.CardMonitoring import CardMonitor,CardMonitoringThread,CardObserver

class MyCardObserver(CardObserver):
    def update(self, observable, (addedcards, removedcards)):
        print addedcards
        print removedcards

class Dlg_SimpleCardMonitor(QDialog,uiCardMonitor.Ui_Dialog):
    connection = None

    def __init__(self, parent=None):
        super(Dlg_SimpleCardMonitor, self).__init__(parent)
        self.setupUi(self)
        self.makeSignalSlot()
        self.myUi()


    def myUi(self):
        for rd in self.getReaderList():
            self.cb_readers.addItem(rd.name)

    def makeSignalSlot(self):
        self.pb_connect.clicked.connect(self.connectReader)

    def connectReader(self):
        for rd in self.getReaderList():
            if rd.name == self.cb_readers.currentText():
                self.connection = rd.createConnection()
                self.tb_response.setText('[ %s ] is connected'%self.connection.getReader())
                print self.connection.getReader()
                break
        cardmonitor = CardMonitor()
        myObserver = MyCardObserver()
        cardmonitor.addObserver(myObserver)


    def getReaderList(self):
        return readers()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg=Dlg_SimpleCardMonitor()
    dlg.show()
    dlg.exec_()

