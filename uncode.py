#coding=gbk
from PyQt4 import QtGui,QtCore,QtSql,QtXml
import sys,time

class Test(QtGui.QWidget):
    def __init__(self,parent=None):
        self.app=QtGui.QApplication([])
        super(Test,self).__init__(parent)
        self.setGeometry(342,231,347,288)
        self.layvTop=QtGui.QVBoxLayout()
        self.setLayout(self.layvTop)
        
        self.lineEdit = QtGui.QLineEdit()
        self.layvTop.addWidget(self.lineEdit)
        self.btn=QtGui.QPushButton(u'解码')
        self.layvTop.addWidget(self.btn)
        self.btn.clicked.connect(
            self.btn_Clicked)
        self.txt=QtGui.QTextEdit()
        self.layvTop.addWidget(self.txt)
    def write(self,txt):
        self.txt.textCursor().insertText(txt)
    def show(self):
        super(Test,self).show()
        self.app.exec_()
    def btn_Clicked(self,event=False):
        if self.lineEdit.text() :
            s=self.lineEdit.text().replace('%u','\u')
            print str(s.toUtf8()).decode('unicode_escape')

if __name__=='__main__':
    t=Test()
    sys.stdout=t
    t.show()
