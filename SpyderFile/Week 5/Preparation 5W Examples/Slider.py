#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we connect a signal
of a QtGui.QSlider to a slot 
of a QtGui.QLCDNumber. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLineEdit
from PyQt5.QtCore import Qt

class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def printSlider(self,val):

        print val
        print type(val)
        print self.sld.value()

        
    def initUI(self):
        self.ql = QLineEdit(self)
        self.ql.move(15,30)
        self.ql.textChanged.connect(self.syncSlider)
        self.ql.setMinimumWidth(200)
        
        
        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.valueChanged.connect(self.syncText)
        self.sld.move(15,0)
        self.sld.setMinimumWidth(200)

        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()
        
    def syncText(self, text):
        self.ql.setText(str(self.sld.value()))
    
    def syncSlider(self, val):
        try:
            value = int(val)
        except:
            value = 0
        
        value = max(self.sld.minimum(), value)
        value = min(self.sld.maximum(), value)
        self.sld.setValue(value)
        
        
def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()

if __name__ == '__main__':
    main()
