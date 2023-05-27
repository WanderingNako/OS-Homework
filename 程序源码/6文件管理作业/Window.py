from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QStackedWidget,\
    QPushButton,QHBoxLayout,QSizePolicy,QStackedLayout,QFormLayout,QLineEdit,QTableWidget,\
    QTableWidgetItem,QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from random import *
from FM import *
import sys
import os


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('File Management')
        self.resize(644, 575)
        self.table = FreeBlockTable(1, 500)

        layout = QHBoxLayout()
        # 表格对象
        self.tableWidget = QTableWidget()
        # 显示初始空闲表
        self.showtable()

        # 按钮布局器
        layout_middle = QVBoxLayout()

        # 按钮
        button_1 = QPushButton()
        button_1.setText("随机添加50个文件")
        button_2 = QPushButton()
        button_2.setText("删除奇数文件")
        button_3 = QPushButton()
        button_3.setText("添加ABCDE文件")
        button_4 = QPushButton()
        button_4.setText("查看ABCDE文件存储状态")

        self.tableWidget2 = QTableWidget()

        layout_middle.addWidget(button_1)
        layout_middle.addWidget(button_2)
        layout_middle.addWidget(button_3)
        layout_middle.addWidget(button_4)
        layout_middle.addWidget(self.tableWidget2)


        # 布局管理
        layout.addWidget(self.tableWidget, 2)
        layout.addStretch()
        layout.addLayout(layout_middle, 3)
        self.setLayout(layout)

        #信号与槽
        button_1.clicked.connect(self.button_1)
        button_2.clicked.connect(self.button_2)
        button_3.clicked.connect(self.button_3)
        button_4.clicked.connect(self.button_4)

    def showtable(self):
        # 设置表格大小
        self.tableWidget.setRowCount(self.table.table.shape[0])
        self.tableWidget.setColumnCount(self.table.table.shape[1])
        # 设置表格字段
        self.tableWidget.setHorizontalHeaderLabels(['起始位置', '空闲磁盘块数'])
        # 设置表格内容
        for i in range(self.table.table.shape[0]):
            for j in range(2):
                newItem = QTableWidgetItem(str(self.table.table.iloc[i][j]))
                newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
                self.tableWidget.setItem(i, j, newItem)

    # 随机添加50个文件
    def button_1(self):
        self.allocateStartList = []
        self.allocateSizeList = []
        for i in range(1, 51):
            x = random.randint(1, 5)
            self.allocateStartList.append(self.table.allocate(x))
            self.allocateSizeList.append(x)
        self.showtable()

    # 删除奇数文件
    def button_2(self):
        for i in range(1, 51):
            if i % 2 == 1:
                self.table.deallocate(self.allocateStartList[i - 1], self.allocateSizeList[i - 1])
        self.showtable()

    # 添加ABCDE文件
    def button_3(self):
        txtList = [7, 5, 2, 9, 3.5]
        self.blockList = []
        for txt in txtList:
            x = int(txt / 2)
            if int(txt / 2) < txt / 2:
                x = int(txt / 2) + 1
            self.blockList.append(x)
        self.letterStartList = []
        for x in self.blockList:
            self.letterStartList.append(self.table.allocate(x))
        self.showtable()

    # 查看ABCDE文件存储状态
    def button_4(self):
        # 设置表格大小
        self.tableWidget2.setRowCount(5)
        self.tableWidget2.setColumnCount(3)
        # 设置表格字段
        self.tableWidget2.setHorizontalHeaderLabels(['文件名','存储起始位置', '占用磁盘块数'])
        # 设置表格内容
        for i in range(5):
            newItem = QTableWidgetItem(chr(65+i)+'.txt')
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget2.setItem(i, 0, newItem)
            newItem = QTableWidgetItem(str(self.letterStartList[i]))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget2.setItem(i, 1, newItem)
            newItem = QTableWidgetItem(str(self.blockList[i]))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget2.setItem(i, 2, newItem)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    # styleFile = 'res/button.qss'
    # qssStyle = CommonHelper.readQss(styleFile)
    # window.setStyleSheet(qssStyle)
    window.show()
    sys.exit(app.exec_())