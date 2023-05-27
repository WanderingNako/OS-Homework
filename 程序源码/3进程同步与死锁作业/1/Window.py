from PyQt5.QtWidgets import QApplication,\
    QWidget,QVBoxLayout,QLabel,QStackedWidget,QPushButton,\
    QHBoxLayout,QSizePolicy,QStackedLayout,QFormLayout,QLineEdit,\
    QTableWidget,QTableWidgetItem,QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from random import *
from ProducerAndConsumer import *
import sys
import os


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('Producer/consumer')
        self.resize(326, 200)



        layout = QHBoxLayout()
        layout_left = QVBoxLayout()
        # 标签布局管理器
        layout_label = QHBoxLayout()
        # 标签
        producer_label = QLabel()
        producer_label.setText("生产者进程数量：5")
        consumer_label = QLabel()
        consumer_label.setText("消费者进程数量：5")

        layout_label.addWidget(producer_label)
        layout_label.addWidget(consumer_label)

        # # 表格对象
        # self.tableWidget = QTableWidget()
        # # 10行1列
        # self.tableWidget.setRowCount(10)
        # self.tableWidget.setColumnCount(1)
        # # 设置单元格宽度
        # for j in range(10):
        #     self.tableWidget.setColumnWidth(j, 200)
        # # 设置表格字段
        # self.tableWidget.setHorizontalHeaderLabels(['产品共享缓冲区'])
        self.textEdit = QTextEdit()

        # 按钮布局器
        layout_button = QVBoxLayout()
        # 按钮
        reset_button = QPushButton()
        reset_button.setText("重置")
        start_button = QPushButton()
        start_button.setText("开始并显示")

        layout_button.addWidget(reset_button)
        layout_button.addWidget(start_button)

        # 显示初始列表
        self.reset_button()

        # 布局管理
        layout_left.addLayout(layout_label)
        layout_left.addWidget(self.textEdit)
        layout.addLayout(layout_left)
        layout.addLayout(layout_button)
        self.setLayout(layout)

        # 信号与槽
        reset_button.clicked.connect(self.reset_button)
        start_button.clicked.connect(self.start_button)


    def start(self):
        # 创建共享队列
        self.q = mp.Manager().list()
        # 创建信号量
        self.empty = mp.Semaphore(10)
        self.full = mp.Semaphore(0)
        self.num_processes = 5
        self.processes = []
        for i in range(self.num_processes):
            self.processes.append(mp.Process(target=producer, args=(self.q, self.empty, self.full)))
            self.processes.append(mp.Process(target=consumer, args=(self.q, self.empty, self.full)))
        # 启动所有进程
        for p in self.processes:
            p.start()

    def reset_button(self):
        # 清除txt文件内容
        with open("output.txt", "w", encoding="UTF-8") as f:
            f.truncate(0)
        # 清除文本内容
        self.textEdit.setText("")
        self.start()

    def start_button(self):
        # 显示txt
        with open("output.txt", 'r', encoding="UTF-8") as f:
            data = f.read()
            self.textEdit.setText(data)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    # styleFile = 'res/button.qss'
    # qssStyle = CommonHelper.readQss(styleFile)
    # window.setStyleSheet(qssStyle)
    window.show()
    sys.exit(app.exec_())