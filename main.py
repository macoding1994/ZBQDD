# -*- coding: utf-8 -*-
import os
import sys
import xlrd
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from Ui_main import Ui_MainWindow
from lib.func import linearity,total_uncertainty


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.xdata = []
        self.ydata = []
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        '''打开execl'''
        self.lineEdit.clear()
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                "选取文件",
                                                                os.getcwd(),  # 起始路径
                                                                "Excel Files (*.xlsx);;All Files (*)")  # 设置文件扩展名过滤,用双分号间隔
        self.lineEdit.setText(fileName_choose)
        try:
            data = xlrd.open_workbook(fileName_choose)
            table = data.sheets()[0]
        except Exception as e:
            self.warning('清选择正确的文件格式')
            return

        for i in range(1,table.nrows):
            for j in range(1,table.ncols):
                if j == 1:
                    self.xdata.append(table.cell(i,j).value)
                else:
                    self.ydata.append(table.cell(i,j).value)
        else:
            print(self.xdata,self.ydata)
            self.widget.generateData(self.xdata,self.ydata)


    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        '''执行函数'''
        if self.xdata and self.ydata:
            y_l = linearity(self.xdata[:6],self.ydata[:6])
            print('%.2f%%' % (y_l * 100))
            k, b, y_f_s, lhr = total_uncertainty(self.xdata,self.ydata)
            print(k, b, y_f_s, '%.2f%%' % (lhr * 100))

    def warning(self,str):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('警告')
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(str)
        # msgBox.setInformativeText('出现更改愿意保存吗?')
        Yes = msgBox.addButton('是', QMessageBox.AcceptRole)
        msgBox.setDefaultButton(Yes)
        reply = msgBox.exec()



def main():
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
