class Sstf:
    def __init__(self, start, data):
        self.start = start # 起始位置
        self.data = data # 磁盘请求序列
        self.length = 0 # 寻道总长
        self.averageL = 0 # 平均寻道长度
        self.outList = [] # 输出列表

    def findNextIndex(self, start, datas):
        length = []
        for data in datas:
            l = abs(int(start) - int(data))
            length.append(l)
        minIndex = length.index(min(length))
        return minIndex


    def loadNext(self, now, next):
        length = abs(int(now) - int(next))
        self.outList.append([str(next),str(length)])
        return length

    def deal(self):
        data2 = self.data.split().copy()
        n = len(data2)
        for d in self.data.split():
            nextIndex = self.findNextIndex(self.start, data2)
            self.length += self.loadNext(self.start, data2[nextIndex])
            self.start = data2[nextIndex]
            data2.remove(data2[nextIndex])
        self.averageL = round(self.length / n, 2)

if __name__ == '__main__':
    start = '100'
    data = '55 58 39 18 90 160 150 38 184'
    # data2 = data.split().copy()
    # n = len(data2)
    # print("下一个磁道\t磁头移动距离")
    # for d in data.split():
    #     nextIndex = findNextIndex(start, data2)
    #     l += loadNext(start, data2[nextIndex])
    #     start = data2[nextIndex]
    #     data2.remove(data2[nextIndex])
    #
    # print("SSTF:寻道总长度："+ str(l))
    # print("SSTF:平均寻道长度：%.1f" % (l / n))
    sstf = Sstf(start,data)
    sstf.deal()
    print(sstf.outList)
    print(sstf.length)
    print(sstf.averageL)

