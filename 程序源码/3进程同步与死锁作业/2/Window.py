from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QStackedWidget,\
    QPushButton,QHBoxLayout,QSizePolicy,QStackedLayout,QFormLayout,QLineEdit,QTableWidget,\
    QTableWidgetItem,QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from random import *
from Bank import bank
import sys
import os

procx = ['P1', 'P2', 'P3', 'P4', 'P5']#进程
allocationx = ['2\t1\t2', '4\t0\t2', '4\t0\t5', '2\t0\t4', '3\t1\t4']#分配矩阵
max_x = ['5\t5\t9', '5\t3\t6', '4\t0\t11', '4\t2\t5', '4\t2\t4']#最大需求矩阵

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('Bankers')
        self.resize(710, 270)

        layout = QHBoxLayout()
        layout_left = QVBoxLayout()
        label1 = QLabel()
        label1.setText("资源总数：A:17\t B:5\tC:20")
        layout_left.addWidget(label1)
        # 表格对象
        self.tableWidget = QTableWidget()
        # 表格大小
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)
        # 设置表格字段
        self.tableWidget.setHorizontalHeaderLabels(['进程', '最大资源需求量', '已分配资源数量'])
        # 不显示行号
        self.tableWidget.verticalHeader().setVisible(False)
        # 为表格添加内容
        newItem = QTableWidgetItem('A\tB\tC')
        newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('A\tB\tC')
        newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.tableWidget.setItem(0, 2, newItem)
        for i in range(1,6):
            newItem = QTableWidgetItem(procx[i-1])
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget.setItem(i, 0, newItem)
            newItem = QTableWidgetItem(max_x[i-1])
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget.setItem(i, 1, newItem)
            newItem = QTableWidgetItem(allocationx[i-1])
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget.setItem(i, 2, newItem)

        # 输出label
        self.out_label = QLabel()

        layout_left.addWidget(self.tableWidget)
        layout_left.addWidget(self.out_label)

        # 按钮布局器
        layout_right = QVBoxLayout()

        # 按钮
        safe_button = QPushButton()
        safe_button.setText("安全性检查")
        proc_label = QLabel()
        proc_label.setText("请求资源的进程：")
        self.text_proc = QLineEdit()
        a_label = QLabel()
        a_label.setText("申请A资源：")
        self.text_a = QLineEdit()
        b_label = QLabel()
        b_label.setText("申请B资源：")
        self.text_b = QLineEdit()
        c_label = QLabel()
        c_label.setText("申请C资源：")
        self.text_c = QLineEdit()
        bank_button = QPushButton()
        bank_button.setText("能否分配？")


        layout_right.addWidget(safe_button)
        layout_bank = QVBoxLayout()

        layout_1 = QHBoxLayout()
        layout_2 = QHBoxLayout()
        layout_3 = QHBoxLayout()
        layout_4 = QHBoxLayout()

        layout_1.addWidget(proc_label)
        layout_1.addWidget(self.text_proc)
        layout_2.addWidget(a_label)
        layout_2.addWidget(self.text_a)
        layout_3.addWidget(b_label)
        layout_3.addWidget(self.text_b)
        layout_4.addWidget(c_label)
        layout_4.addWidget(self.text_c)

        layout_bank.addLayout(layout_1)
        layout_bank.addLayout(layout_2)
        layout_bank.addLayout(layout_3)
        layout_bank.addLayout(layout_4)
        layout_bank.addWidget(bank_button)

        layout_right.addLayout(layout_bank)


        # 布局管理
        layout.addLayout(layout_left, 2)
        layout.addStretch()
        layout.addLayout(layout_right, 1)
        self.setLayout(layout)

        #信号与槽
        safe_button.clicked.connect(self.safe_button)
        bank_button.clicked.connect(self.bank_button)


    def safe_button(self):
        start = 'P1'
        request = ['0', '0', '0']
        if bank(start, request) != None:
            self.out_label.setText("目前处于安全状态，存在安全序列："+str(bank(start, request)))
        else:
            self.out_label.setText("目前处于不安全状态，有可能发生死锁！")


    def bank_button(self):
        start = self.text_proc.text()
        request = []
        a = self.text_a.text()
        b = self.text_b.text()
        c = self.text_c.text()
        request.append(a)
        request.append(b)
        request.append(c)
        if bank(start, request) != None:
            self.out_label.setText("可以分配，存在安全序列："+str(bank(start, request)))
        else:
            self.out_label.setText("无法分配！")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    # styleFile = 'res/button.qss'
    # qssStyle = CommonHelper.readQss(styleFile)
    # window.setStyleSheet(qssStyle)
    window.show()
    sys.exit(app.exec_())