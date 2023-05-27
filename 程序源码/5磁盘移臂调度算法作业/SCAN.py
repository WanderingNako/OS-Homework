class Scan:
    def __init__(self, start, data):
        self.start = start  # 起始位置
        self.data = data  # 磁盘请求序列
        self.length = 0  # 寻道总长
        self.averageL = 0  # 平均寻道长度
        self.outList = []  # 输出列表

    def loadNext(self, now, next):
        length = abs(int(now) - int(next))
        self.outList.append([str(next), str(length)])
        return length


    def findNext(self, now, data):
        biggerList = []
        smallerList = []
        for d in data:
            if int(d) > int(now):
                biggerList.append(d)
        if (len(biggerList) == 0):
            if len(data) != 0:
                for d2 in data:
                    if int(d2) < int(now):
                        smallerList.append(d2)
                return max(smallerList)
            else:
                return None
        return min(biggerList)

    def deal(self):
        data2 = self.data.split().copy()
        n = len(data2)
        for d in self.data:
            next = self.findNext(self.start, data2)
            if next == None:
                break
            self.length += self.loadNext(self.start, next)
            self.start = next
            data2.remove(next)
        self.averageL = round(self.length / n, 2)


if __name__ == '__main__':
    start = '100'
    data = '55 58 39 18 90 160 150 38 184'
    # data2 = data.split().copy()
    # n = len(data2)
    # print("下一个磁道\t磁头移动距离")
    # for d in data:
    #     next = findNext(start, data2)
    #     if next == None:
    #         break
    #     l += loadNext(start, next)
    #     start = next
    #     data2.remove(next)
    #
    # print("SCAN:寻道总长度："+ str(l))
    # print("SCAN:平均寻道长度：%.1f" % (l / n))
    scan = Scan(start,data)
    scan.deal()
    print(scan.outList)
    print(scan.length)
    print(scan.averageL)