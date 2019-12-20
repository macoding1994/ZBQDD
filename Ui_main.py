# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python\pyqt\ZBQDD\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setMinimumSize(QtCore.QSize(750, 450))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = MyGraph(self.groupBox)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 1, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "中科飞龙数据展示软件"))
        self.groupBox.setTitle(_translate("MainWindow", "画图"))
        self.groupBox_3.setTitle(_translate("MainWindow", "显示"))
        self.label_2.setText(_translate("MainWindow", "总不确定度："))
        self.groupBox_2.setTitle(_translate("MainWindow", "按钮"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "3"))
        self.label.setText(_translate("MainWindow", "文件路径："))
        self.label_3.setText(_translate("MainWindow", "结构调整："))
        self.pushButton.setText(_translate("MainWindow", "预览"))
        self.pushButton_2.setText(_translate("MainWindow", "执行"))
from graph import MyGraph


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
