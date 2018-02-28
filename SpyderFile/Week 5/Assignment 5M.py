# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 18:04:40 2018

@author: Xiang Yang Ng
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor, QPainter

class BallBouncing(QWidget):
    def __init__(self):
        super(BallBouncing, self).__init__()
        self.initUI()
        
    def initUI(self):
        #Position, diamater and speed of ball on the window
        self.d = 30; self.x = 0; self.y = 0
        self.dx = 3; self.dy = 3
              
        #timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.Animate)
        self.timer.start(10)
        
        #Initializing Widget
        self.setGeometry(300, 300, 600, 400)
     
        self.setWindowTitle('Animation')
        self.show()
      
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
    
    def drawRectangles(self, qp):
        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(0, 0, self.width(), self.height())
        qp.setBrush(QColor(200, 0, 0))
        qp.drawEllipse(self.x, self.y, self.d, self.d)
        
    def Animate(self):
        self.x += self.dx
        self.y += self.dy
        self.CheckCollision()
        self.update()
                
    def CheckCollision(self):
        if (self.x <= 0) or ((self.x + self.d)== self.width()):
            self.dx = -self.dx
            
        elif self.x + self.d > self.width():
            self.x = self.width() - self.d
            self.dx = -self.dx
            
        if (self.y <= 0):
            self.dy = abs(self.dy)
            
        elif ((self.y + self.d) == self.height()):
            self.dy = -self.dy
        
        elif self.y + self.d > self.height():
            self.y = self.height() - self.d
            self.dy = -self.dy
    

        
def main():
    
    app = QApplication(sys.argv)
    bb = BallBouncing()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()