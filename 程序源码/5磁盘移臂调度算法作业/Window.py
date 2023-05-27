from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QStackedWidget,\
    QPushButton,QHBoxLayout,QSizePolicy,QStackedLayout,QFormLayout,QLineEdit,QTableWidget,\
    QTableWidgetItem,QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from random import *
from SSTF import *
from SCAN import *
import sys
import os


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('Disk Scheduling')
        self.resize(454, 524)

        layout = QHBoxLayout()
        layout_left = QVBoxLayout()
        # 表格对象
        self.tableWidget = QTableWidget()


        # 磁臂移动总量label
        self.all_label = QLabel()
        # 磁臂平均移动量label
        self.ave_label = QLabel()

        layout_left.addWidget(self.tableWidget)
        layout_left.addWidget(self.all_label)
        layout_left.addWidget(self.ave_label)

        # 按钮布局器
        layout_right = QVBoxLayout()

        # 按钮
        seq_label = QLabel()
        seq_label.setText("磁盘请求序列（空格隔开）：")
        self.text_seq = QLineEdit()
        start_label = QLabel()
        start_label.setText("起始位置：")
        self.text_start = QLineEdit()
        sstf_button = QPushButton()
        sstf_button.setText("SSTF")
        scan_button = QPushButton()
        scan_button.setText("SCAN")

        layout_1 = QHBoxLayout()
        layout_2 = QHBoxLayout()

        layout_1.addWidget(seq_label)
        layout_1.addWidget(self.text_seq)
        layout_2.addWidget(start_label)
        layout_2.addWidget(self.text_start)

        layout_right.addLayout(layout_1)
        layout_right.addLayout(layout_2)
        layout_right.addWidget(sstf_button)
        layout_right.addWidget(scan_button)


        # 布局管理
        layout.addLayout(layout_left, 2)
        layout.addStretch()
        layout.addLayout(layout_right, 1)
        self.setLayout(layout)

        #信号与槽
        sstf_button.clicked.connect(self.sstf_button)
        scan_button.clicked.connect(self.scan_button)



    def sstf_button(self):
        start = self.text_start.text()
        data = self.text_seq.text()
        sstf = Sstf(start, data)
        sstf.deal()

        # 表格大小
        self.tableWidget.setRowCount(len(data.split()))
        self.tableWidget.setColumnCount(2)
        # 设置表格字段
        self.tableWidget.setHorizontalHeaderLabels(['下一个磁道', '磁头移动距离'])
        # 为表格添加内容
        for i in range(len(sstf.outList)):
            for j in range(2):
                    newItem = QTableWidgetItem(str(sstf.outList[i][j]))
                    newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
                    self.tableWidget.setItem(i, j, newItem)
        self.all_label.setText('寻道总长：'+str(sstf.length))
        self.ave_label.setText('平均寻道长度：'+str(sstf.averageL))


    def scan_button(self):
        start = self.text_start.text()
        data = self.text_seq.text()
        scan = Scan(start, data)
        scan.deal()

        # 表格大小
        self.tableWidget.setRowCount(len(data.split()))
        self.tableWidget.setColumnCount(2)
        # 设置表格字段
        self.tableWidget.setHorizontalHeaderLabels(['下一个磁道', '磁头移动距离'])
        # 为表格添加内容
        for i in range(len(scan.outList)):
            for j in range(2):
                newItem = QTableWidgetItem(str(scan.outList[i][j]))
                newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
                self.tableWidget.setItem(i, j, newItem)
        self.all_label.setText('寻道总长：' + str(scan.length))
        self.ave_label.setText('平均寻道长度：' + str(scan.averageL))

if __name__ == "__main__":
    s = "55 58 39 18 90 160 150 38 184"
    app = QApplication(sys.argv)
    window = Window()
    # styleFile = 'res/button.qss'
    # qssStyle = CommonHelper.readQss(styleFile)
    # window.setStyleSheet(qssStyle)
    window.show()
    sys.exit(app.exec_())