from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QStackedWidget,\
    QPushButton,QHBoxLayout,QSizePolicy,QStackedLayout,QFormLayout,QLineEdit,QTableWidget,\
    QTableWidgetItem,QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from random import *
from RAM import *
import sys
import os


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('Memory Management')
        self.resize(1559, 293)

        layout = QHBoxLayout()
        layout_left = QVBoxLayout()
        # 表格对象
        self.tableWidget = QTableWidget()

        # 输出淘汰序列label
        self.out_label = QLabel()
        # 缺页次数label
        self.count_label = QLabel()
        # 缺页率label
        self.ratio_label = QLabel()

        layout_left.addWidget(self.tableWidget)
        layout_left.addWidget(self.out_label)
        layout_left.addWidget(self.count_label)
        layout_left.addWidget(self.ratio_label)

        # 按钮布局器
        layout_right = QVBoxLayout()

        # 按钮
        seq_label = QLabel()
        seq_label.setText("页面引用序列（空格隔开）：")
        self.text_seq = QLineEdit()
        allocate_label = QLabel()
        allocate_label.setText("页面数目：")
        self.text_allocate = QLineEdit()
        opt_button = QPushButton()
        opt_button.setText("OPTIMAL")
        lru_button = QPushButton()
        lru_button.setText("LRU")
        fifo_button = QPushButton()
        fifo_button.setText("FIFO")

        layout_1 = QHBoxLayout()
        layout_2 = QHBoxLayout()

        layout_1.addWidget(seq_label)
        layout_1.addWidget(self.text_seq)
        layout_2.addWidget(allocate_label)
        layout_2.addWidget(self.text_allocate)

        layout_right.addLayout(layout_1)
        layout_right.addLayout(layout_2)
        layout_right.addWidget(opt_button)
        layout_right.addWidget(lru_button)
        layout_right.addWidget(fifo_button)


        # 布局管理
        layout.addLayout(layout_left, 2)
        layout.addStretch()
        layout.addLayout(layout_right, 1)
        self.setLayout(layout)

        #信号与槽
        opt_button.clicked.connect(self.opt_button)
        lru_button.clicked.connect(self.lru_button)
        fifo_button.clicked.connect(self.fifo_button)



    def opt_button(self):
        blocknum = int(self.text_allocate.text())
        page = list(map(int, self.text_seq.text().split()))
        optimal = Optimal(blocknum=blocknum, page=page)
        PageList = optimal.deal()
        # 表格大小
        self.tableWidget.setRowCount(blocknum)
        self.tableWidget.setColumnCount(len(PageList))
        for i in range(len(PageList)):
            self.tableWidget.setColumnWidth(i, 50)
        # 设置表格字段
        self.tableWidget.setHorizontalHeaderLabels([str(i) for i in page])
        # 为表格添加内容
        for i in range(blocknum):
            for j in range(len(PageList)):
                if PageList[j][i] != -1:
                    newItem = QTableWidgetItem(str(PageList[j][i]))
                    newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
                    self.tableWidget.setItem(i, j, newItem)
                else:
                    newItem = QTableWidgetItem('')
                    newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
                    self.tableWidget.setItem(i, j, newItem)
        self.out_label.setText('淘汰序列：'+str(optimal.outList))
        self.count_label.setText('缺页次数：'+str(optimal.getNumberOfLackPage()))
        self.ratio_label.setText('缺页率：'+str(round(optimal.getNumberOfLackPage()/optimal.getNumberOfPage()*100, 2))+'%')


    def lru_button(self):
        blocknum = int(self.text_allocate.text())
        page = list(map(int, self.text_seq.text().split()))
        lru = Lru(blocknum=blocknum, page=page)
        PageList = lru.deal()
        # 表格大小
        self.tableWidget.setRowCount(blocknum)
        self.tableWidget.setColumnCount(len(PageList))
        for i in range(len(PageList)):
            self.tableWidget.setColumnWidth(i, 50)
        # 设置表格字段
        self.tableWidget.setHorizontalHeaderLabels([str(i) for i in page])
        # 为表格添加内容
        for i in range(blocknum):
            for j in range(len(PageList)):
                if PageList[j][i] != -1:
                    newItem = QTableWidgetItem(str(PageList[j][i]))
                    newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
                    self.tableWidget.setItem(i, j, newItem)
                else:
                    newItem = QTableWidgetItem('')
                    newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
                    self.tableWidget.setItem(i, j, newItem)
        self.out_label.setText('淘汰序列：' + str(lru.outList))
        self.count_label.setText('缺页次数：' + str(lru.getNumberOfLackPage()))
        self.ratio_label.setText('缺页率：' + str(round(lru.getNumberOfLackPage() / lru.getNumberOfPage() * 100, 2)) + '%')


    def fifo_button(self):
        blocknum = int(self.text_allocate.text())
        page = list(map(int, self.text_seq.text().split()))
        fifo = Fifo(blocknum=blocknum, page=page)
        PageList = fifo.deal()
        # 表格大小
        self.tableWidget.setRowCount(blocknum)
        self.tableWidget.setColumnCount(len(PageList))
        for i in range(len(PageList)):
            self.tableWidget.setColumnWidth(i, 50)
        # 设置表格字段
        self.tableWidget.setHorizontalHeaderLabels([str(i) for i in page])
        # 为表格添加内容
        for i in range(blocknum):
            for j in range(len(PageList)):
                if PageList[j][i] != -1:
                    newItem = QTableWidgetItem(str(PageList[j][i]))
                    newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
                    self.tableWidget.setItem(i, j, newItem)
                else:
                    newItem = QTableWidgetItem('')
                    newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
                    self.tableWidget.setItem(i, j, newItem)
        self.out_label.setText('淘汰序列：' + str(fifo.outList))
        self.count_label.setText('缺页次数：' + str(fifo.getNumberOfLackPage()))
        self.ratio_label.setText('缺页率：' + str(round(fifo.getNumberOfLackPage() / fifo.getNumberOfPage() * 100, 2)) + '%')


if __name__ == "__main__":
    s = "7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1"
    app = QApplication(sys.argv)
    window = Window()
    # styleFile = 'res/button.qss'
    # qssStyle = CommonHelper.readQss(styleFile)
    # window.setStyleSheet(qssStyle)
    window.show()
    sys.exit(app.exec_())