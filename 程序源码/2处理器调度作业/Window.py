from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QStackedWidget,QPushButton,QHBoxLayout,QSizePolicy,QStackedLayout,QFormLayout,QLineEdit,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from random import *
from Homework import *
import sys
import os


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('Scheduling')
        self.resize(547, 388)



        layout = QVBoxLayout()
        layout_top = QHBoxLayout()
        # 表格对象
        self.tableWidget = QTableWidget()
        # 五行三列
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        # 设置表格字段
        self.tableWidget.setHorizontalHeaderLabels(['进程', '到达时间', '服务时间'])

        # 按钮布局器
        layout_button = QVBoxLayout()
        # 按钮
        reset_button = QPushButton()
        reset_button.setText("重置")
        fcfs_button = QPushButton()
        fcfs_button.setText("FCFS")
        rr_button = QPushButton()
        rr_button.setText("RR")
        sjf_button = QPushButton()
        sjf_button.setText("SJF")
        hrn_button = QPushButton()
        hrn_button.setText("HRN")

        layout_button.addWidget(reset_button)
        layout_button.addWidget(fcfs_button)
        layout_button.addWidget(rr_button)
        layout_button.addWidget(sjf_button)
        layout_button.addWidget(hrn_button)

        # 输出表格对象
        self.tableWidget_out = QTableWidget()
        # 五行五列
        self.tableWidget_out.setRowCount(5)
        self.tableWidget_out.setColumnCount(5)
        # 设置表格字段
        self.tableWidget_out.setHorizontalHeaderLabels(['进程', '开始执行时间', '完成时间', '周转时间', '带权周转时间'])

        # 显示初始列表
        self.reset_button()

        # 布局管理
        layout_top.addWidget(self.tableWidget)
        layout_top.addLayout(layout_button)
        layout.addLayout(layout_top)
        layout.addWidget(self.tableWidget_out)
        self.setLayout(layout)

        # 信号与槽
        reset_button.clicked.connect(self.reset_button)
        fcfs_button.clicked.connect(self.fcfs_button)
        sjf_button.clicked.connect(self.sjf_button)
        hrn_button.clicked.connect(self.hrn_button)
        rr_button.clicked.connect(self.rr_button)

    def reset_button(self):
        # 随机生成到达时间和服务时间
        self.InputTime = [0]
        self.ServeTime = []
        for i in range(4):
            self.InputTime.append(randint(0, 20))
            self.ServeTime.append(randint(1, 20))
        self.ServeTime.append(randint(1, 20))
        # 原始表格
        for i in range(5):
            newItem = QTableWidgetItem(chr(65+i))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget.setItem(i, 0, newItem)
            newItem = QTableWidgetItem(str(self.InputTime[i]))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget.setItem(i, 1, newItem)
            newItem = QTableWidgetItem(str(self.ServeTime[i]))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget.setItem(i, 2, newItem)
        # 清空结果表格
        self.tableWidget_out.clearContents()

    def fcfs_button(self):
        homework = []
        for i in range(5):
            h = Homework(self.InputTime[i], self.ServeTime[i],chr(65 + i))
            homework.append(h)
        FCFS(homework)
        # 生成表格
        for i in range(5):
            newItem = QTableWidgetItem(homework[i].ID)
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 0, newItem)
            newItem = QTableWidgetItem(str(homework[i].start_time))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 1, newItem)
            newItem = QTableWidgetItem(str(homework[i].end_time))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 2, newItem)
            newItem = QTableWidgetItem(str(homework[i].turn_around))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 3, newItem)
            newItem = QTableWidgetItem(str(homework[i].dai_time))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 4, newItem)

    def sjf_button(self):
        homework = []
        for i in range(5):
            h = Homework(self.InputTime[i], self.ServeTime[i],chr(65 + i))
            homework.append(h)
        list = SJF(homework)
        # 生成表格
        for i in range(5):
            newItem = QTableWidgetItem(list[i].ID)
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 0, newItem)
            newItem = QTableWidgetItem(str(list[i].start_time))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 1, newItem)
            newItem = QTableWidgetItem(str(list[i].end_time))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 2, newItem)
            newItem = QTableWidgetItem(str(list[i].turn_around))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 3, newItem)
            newItem = QTableWidgetItem(str(list[i].dai_time))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 4, newItem)

    def hrn_button(self):
        homework = []
        for i in range(5):
            h = Homework(self.InputTime[i], self.ServeTime[i],chr(65 + i))
            homework.append(h)
        list = HRN(homework)
        # 生成表格
        for i in range(5):
            newItem = QTableWidgetItem(list[i].ID)
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 0, newItem)
            newItem = QTableWidgetItem(str(list[i].start_time))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 1, newItem)
            newItem = QTableWidgetItem(str(list[i].end_time))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 2, newItem)
            newItem = QTableWidgetItem(str(list[i].turn_around))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 3, newItem)
            newItem = QTableWidgetItem(str(list[i].dai_time))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 4, newItem)

    def rr_button(self):
        homework = []
        for i in range(5):
            h = Homework(self.InputTime[i], self.ServeTime[i], chr(65 + i))
            homework.append(h)
        RR(homework)
        # 生成表格
        for i in range(5):
            newItem = QTableWidgetItem(homework[i].ID)
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 0, newItem)
            newItem = QTableWidgetItem('/')
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 1, newItem)
            newItem = QTableWidgetItem(str(homework[i].end_time))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 2, newItem)
            newItem = QTableWidgetItem(str(homework[i].turn_around))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 3, newItem)
            newItem = QTableWidgetItem(str(homework[i].dai_time))
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
            self.tableWidget_out.setItem(i, 4, newItem)


if __name__ == "__main__":
    # h1 = Homework(0, 4)
    # h2 = Homework(1, 3)
    # h3 = Homework(2, 5)
    # h4 = Homework(3, 2)
    # h5 = Homework(4, 4)
    # homework1 = [h1, h2, h3, h4, h5]
    # FCFS(homework1)
    app = QApplication(sys.argv)
    window = Window()
    # styleFile = 'res/button.qss'
    # qssStyle = CommonHelper.readQss(styleFile)
    # window.setStyleSheet(qssStyle)
    window.show()
    sys.exit(app.exec_())