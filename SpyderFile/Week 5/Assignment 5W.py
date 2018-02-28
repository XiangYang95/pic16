# -*- coding: utf-8 -*-
"""
Created on Thu Feb 08 11:11:47 2018

@author: Xiang Yang Ng
"""

from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer

class Example(QWidget):
    
    
    def __init__(self):
        super(Example, self).__init__()        
        self.initUI()
        #To determine whether the square is clicked
        self.mouseClicked = False
        
    def initUI(self):     
        #initializing the color dialog
        self.qcd = QColorDialog(self)
        self.qcd.colorSelected.connect(self.changeSquareColor)
        
        #initializing the square's dimension
        self.x = 20; self.y = 20
        self.d = 50
        
        #start the timer
        self.qt = QTimer()
        self.qt.timeout.connect(self.update)
        self.qt.start(1)
        
        #initializing the color
        self.qc = QColor(255,0,0)

        #initializing the widget's dimension
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Square')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        
    def drawRectangles(self, qp):
        qp.setPen(QColor(0, 0, 0, 255))
        
        #draw the widget
        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(0, 0, self.width(), self.height())
        
        #draw the square
        qp.setBrush(self.qc)
        qp.drawRect(self.x, self.y, self.d, self.d)
        
    def mouseDoubleClickEvent(self,e):
        if self.x <= e.x() and e.x() <= self.x + self.d and (
                self.y <= e.y() and e.y() <= self.y + self.d):         
            self.qcd.open()
        
    def mousePressEvent(self,e):
        #if we click in the square, determine the offset
        if self.x <= e.x() and e.x() <= self.x + self.d and (
                self.y <= e.y() and e.y() <= self.y + self.d): 
            self.deltax = e.x() - self.x
            self.deltay = e.y() - self.y
            self.mouseClicked = True
        
    def mouseMoveEvent(self,e):
        #drag the square when it is moved
        if self.mouseClicked:
            self.x = e.x() - self.deltax
            self.y = e.y() - self.deltay

    def mouseReleaseEvent(self,e):
        self.mouseClicked = False
     
    def changeSquareColor(self, color):
        self.qc = self.qcd.currentColor()
             
def main():
    
    app = QApplication([])
    ex = Example()
    app.exec_()


if __name__ == '__main__':
    main()