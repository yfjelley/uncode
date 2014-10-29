#coding=gbk
from PyQt4 import QtGui,QtCore,QtSql,QtXml
import sys

class Test(QtGui.QWidget):
    def __init__(self,parent=None):
        self.app=QtGui.QApplication([])
        super(Test,self).__init__(parent)
       
        self.setGeometry(342,231,347,288)
        self.layvTop=QtGui.QVBoxLayout()
        self.setLayout(self.layvTop)
       
        self.btnPrintHelloWorldToStdout=QtGui.QPushButton('PrintHelloWorldToStdout')
        self.layvTop.addWidget(self.btnPrintHelloWorldToStdout)
       
        self.btnPrintHelloWorldToStdout.clicked.connect(
            self.btnPrintHelloWorldToStdout_Clicked)
           
        self.txt=QtGui.QTextEdit()
        self.layvTop.addWidget(self.txt)
    def write(self,txt):
        self.txt.textCursor().insertText(txt)
    def show(self):
        super(Test,self).show()
        self.app.exec_()
    def btnPrintHelloWorldToStdout_Clicked(self,event=False):
        print 'Hello world!'

if __name__=='__main__':
    t=Test()
    sys.stdout=t
    t.show()