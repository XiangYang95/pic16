from PyQt5.QtWidgets import QWidget, QApplication

class MyWidget(QWidget):
    
    def __init__(self):
        super(MyWidget, self).__init__()        
        self.initialize()
        
    def initialize(self):      
         
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Mouse Press')
        self.show()

    def mousePressEvent(self,e):
        print "Mouse Press"
        print e.x()
        print e.y()
        print e.button()
        
         
def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if __name__ == '__main__':
    main()