# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printHam_widget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QPushButton
from PyQt5.QtCore import QMetaObject, QCoreApplication

class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUI(self)
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PrintHam = QPushButton(Form)
        self.PrintHam.setObjectName("PrintHam")
        self.horizontalLayout.addWidget(self.PrintHam)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Super Ham"))
        self.PrintHam.setText(_translate("Form", "Print Ham"))
        self.PrintHam.clicked.connect(self.PrintHam)
        
    def PrintHam(self):
        print "Ham"
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())

