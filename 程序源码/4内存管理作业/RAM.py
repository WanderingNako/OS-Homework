# 最佳淘汰算法(OPT)
class Optimal:
    def __init__(self, blocknum, page):
        self.page = page   # 访问页面序列
        self.blocknum = blocknum  # 物理块数
        self.lacknum = 0  # 缺页数
        self.outList = [] # 淘汰序列

    # 获取缺页次数
    def getNumberOfLackPage(self):
        return self.lacknum

    # 获取访问序列中的页面数
    def getNumberOfPage(self):
        return self.page.__len__()

    # 输出物理块中的页面
    def output(self, block):
       for i in range(0, len(block)):
           if block[i] != -1:
               print(block[i], end=' ')    # 输出物理块的序列
       print()

    # 寻找淘汰页面
    def search(self, start, block):
        max = -1
        index = -1
        for i in range(0, len(block)):
            j = start
            for j in range(j, len(self.page)):
                if block[i] == self.page[j]:
                    break
            if max < j:
                max = j
                index = i

        return index

    # 页面调度
    def deal(self):
        pageList = []
        count = 0
        block = [i for i in range(0, self.blocknum)]  # 生成物理块
        for i in range(0, self.blocknum):
            block[i] = -1  # 全部为-1
        for i in range(0, len(self.page)):   # 遍历整个序列的次数
            exists = 0
            for j in range(0, len(block)):
                if block[j] == self.page[i]:   # 判断是否相等
                    exists = 1
                    break            # 是就跳出小循环

            if exists:
                pageList.append(block.copy())
                continue
            else:                     # 不相等,缺页次数加一
                self.lacknum = self.lacknum+1  # 缺业+1

            if count < self.blocknum:
                block[count] = self.page[i]
                count = count+1
            else:
                index = self.search(i+1, block)
                self.outList.append(block[index])
                block[index] = self.page[i]
            # self.output(block)
            pageList.append(block.copy())
        return pageList


# 先进先出算法(FIFO)
class Fifo:
    def __init__(self, blocknum, page):
        self.blocknum = blocknum
        self.page = page
        self.lacknum = 0
        self.outList = []  # 淘汰序列

    def getNumberOfLackPage(self):
        return self.lacknum

    def getNumberOfPage(self):
        return self.page.__len__()

    def output(self, block):
        for i in range(0, len(block)):
            if block[i] != -1:
                print(block[i], end=' ')
        print()

    def deal(self):
        pageList = []
        frist = 0
        count = 0
        block = [i for i in range(0, self.blocknum)]

        for i in range(0, self.blocknum):
            block[i] = -1
        for i in range(0, len(self.page)):
            exists = 0
            for j in range(0, len(block)):
                if block[j] == self.page[i]:
                    exists = 1
                    break

            if exists:
                pageList.append(block.copy())
                continue
            else:
                self.lacknum = self.lacknum +1

            if count < self.blocknum:
                block[count] = self.page[i]
                count = count + 1
            else:
                self.outList.append(block[frist])
                block[frist] = self.page[i]
                frist = frist+1
                if frist >=self.blocknum:
                    frist = 0
            pageList.append(block.copy())
        return pageList


# 最近最少使用算法(LRU)
class Lru:
    def __init__(self, blocknum, page):
        self.blocknum = blocknum
        self.page = page
        self.lacknum = 0
        self.outList = []  # 淘汰序列

    def getNumberOfLackPage(self):
        return self.lacknum

    def getNumberOfPage(self):
        return self.page.__len__()

    def output(self, block):
        size = len(block)
        for i in range(0, size):
            print(block[i], end=' ')
        print()

    def deal(self):
        pageList = []
        block = []

        for i in range(0, self.page.__len__()):
            exists = 0
            j = 0
            for j in range(0, block.__len__()):
                if self.page[i] == block[j]:
                    exists = 1
                    break

            if exists:
                # self.outList.append(block[j])
                del block[j]
            else:
                self.lacknum = self.lacknum + 1
                if block.__len__() >= self.blocknum:
                    self.outList.append(block[0])
                    del block[0]

            block.append(self.page[i])
            bb = []
            for i in range(self.blocknum):
                if i < len(block):
                    bb.append(block[i])
                else:
                    bb.append(-1)
            pageList.append(bb.copy())
        return pageList


if __name__ == "__main__":
    blocknum = 3
    page = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
    # blocknum = input('请输入物理块的个数:')
    # blocknum = int(blocknum)
    # page = list(map(int, input('请输入访问序列(空格隔开, 回车结束输入):').split()))
    # print(type(page))
    # print(page)


    print('----------------------最佳淘汰算法(OPT)---------------------')
    # 最佳淘汰算法(OPT)
    optimal = Optimal(blocknum=blocknum, page=page)
    pageList = optimal.deal()

    print('缺页次数:', optimal.getNumberOfLackPage())
    print('缺页率:', optimal.getNumberOfLackPage()/optimal.getNumberOfPage()*100, "%")
    print('命中率', 100-optimal.getNumberOfLackPage()/optimal.getNumberOfPage()*100, '%')
    print('淘汰序列:'+str(optimal.outList))
    print(pageList)
    print()
    print('---------------------先进先出算法(FIFO)---------------------')
    # 先进先出算法(FIFO)
    fifo = Fifo(blocknum=blocknum, page=page)
    fifo.deal()

    print('缺页次数:', fifo.getNumberOfLackPage())
    print('缺页率:', fifo.getNumberOfLackPage()/fifo.getNumberOfPage()*100, "%")
    print('命中率', 100-fifo.getNumberOfLackPage()/fifo.getNumberOfPage()*100, '%')
    print('淘汰序列:' + str(fifo.outList))
    print('--------------------最近最少使用算法(LRU)--------------------')
    # 最近最少使用算法(LRU)
    lru = Lru(blocknum=blocknum, page=page)
    pp = lru.deal()

    print('缺页次数:', lru.getNumberOfLackPage())
    print('缺页率:', lru.getNumberOfLackPage() / lru.getNumberOfPage() * 100, "%")
    print('命中率', 100 - lru.getNumberOfLackPage() / lru.getNumberOfPage() * 100, '%')
    print('淘汰序列:' + str(lru.outList))
    print(pp)

