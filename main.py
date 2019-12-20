# -*- coding: utf-8 -*-
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import sys
import xlrd
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QTableWidgetItem
from Ui_main import Ui_MainWindow
from lib.func import linearity, total_uncertainty
from showDialog import Dialog as show_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.xdata = []
        self.ydata = []
        self.n = None
        self.showDialog = show_Dialog()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        '''打开execl'''
        self.pushButton.setDisabled(True)
        self.lineEdit.clear()
        self.label_4.clear()
        self.showDialog.tableWidget.clearContents()
        self.xdata = []
        self.ydata = []
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                "选取文件",
                                                                os.getcwd(),  # 起始路径
                                                                "Excel Files (*.xlsx);;All Files (*)")  # 设置文件扩展名过滤,用双分号间隔
        self.lineEdit.setText(fileName_choose)
        try:
            data = xlrd.open_workbook(fileName_choose)
            table = data.sheets()[0]
        except Exception as e:
            self.warning('清选择正确的文件')
            self.pushButton.setDisabled(False)
            return

        self.n = int((table.nrows - 1) / 2)

        for i in range(1, table.nrows):
            for j in range(1, table.ncols):
                if j == 1:
                    self.xdata.append(table.cell(i, j).value)
                else:
                    self.ydata.append(table.cell(i, j).value)
        else:
            for  var  in range(len(self.xdata)):
                row = self.showDialog.tableWidget.rowCount()
                self.showDialog.tableWidget.insertRow(int(row))
                data = QTableWidgetItem(str(self.xdata[var]))
                self.showDialog.tableWidget.setItem(var,0,data)
                data = QTableWidgetItem(str(self.ydata[var]))
                self.showDialog.tableWidget.setItem(var,1,data)
            else:
                self.showDialog.exec()
            self.xdata = self.xdata * int(self.comboBox.currentText())
            self.ydata = self.ydata * int(self.comboBox.currentText())
            if int(self.comboBox.currentText()) == 1:
                self.n = int(self.n / 3)
            self.widget.generateData(self.xdata, self.ydata)
        self.pushButton.setDisabled(False)


    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        '''执行函数'''
        if self.xdata and self.ydata:
            # y_l = linearity(self.xdata[:6], self.ydata[:6])
            # print('%.2f%%' % (y_l * 100))
            try:
                k, b, y_f_s, lhr = total_uncertainty(self.xdata, self.ydata, self.n)
            except Exception as e:
                self.warning('数据结构有误，请重新数据结构后再执行')
                return
            print(k, b, y_f_s, '%.2f%%' % (lhr * 100))
            self.label_4.setText('%.2f%%' % (lhr * 100))
            self.xdata = []
            self.ydata = []
        else:
            self.warning('数据不存在，请重新添加Excel')

    def warning(self, str):
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
