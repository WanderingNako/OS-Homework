import pandas as pd
import random


class FreeBlockTable:
    def __init__(self, start, size):
        self.start = start # 磁盘起始存储位置
        self.size = size # 磁盘总大小
        self.table = pd.DataFrame(data={'start': [start], 'size': [size]}) # 空闲表

    def allocate(self, size):
        # 查找空闲块
        free_blocks = self.table[self.table['size'] >= size]
        if len(free_blocks) == 0:
            return None

        # 分配空闲块
        # 返回分配文件的起始位置
        block = free_blocks.iloc[0]
        if block['size'] > size:
            self.table.loc[free_blocks.index[0],'start'] = block['start'] + size
            self.table.loc[free_blocks.index[0],'size'] = block['size'] - size
        else:
            self.table = self.table[self.table['start'] != block['start']]
        return block['start']

    def deallocate(self, start, size):
        # 归还空闲块
        new_block = {'start': start, 'size': size}

        # 找到需要合并的空闲块
        left_block = self.table[(self.table['start'] + self.table['size']) == start]
        right_block = self.table[self.table['start'] == (start + size)]

        if len(left_block) > 0 and len(right_block) > 0:
            # 左右两边都有空闲块，需要合并
            self.table.loc[left_block.index[0], 'size'] += size + right_block.iloc[0]['size']
            self.table.drop(right_block.index[0], inplace=True)
        elif len(left_block) > 0:
            # 只有左边有空闲块，需要合并
            self.table.loc[left_block.index[0], 'size'] += size
        elif len(right_block) > 0:
            # 只有右边有空闲块，需要合并
            self.table.loc[right_block.index[0], 'start'] = start
            self.table.loc[right_block.index[0], 'size'] += size
        else:
            # 没有相邻的空闲块，直接插入新的空闲块
            self.table = self.table.append(new_block, ignore_index=True)

    def __str__(self):
        return str(self.table)


if __name__ == '__main__':
    # 主程序
    table = FreeBlockTable(1, 500)
    print("---------------------初始空闲表---------------------")
    print(table)
    print("------------------随机添加50个文件-------------------")
    #随机生成 2k-10k 的文件 50 个，文件名为 1.txt、2.txt、……、50.txt
    allocateStartList = []
    allocateSizeList = []
    for i in range(1,51):
        x = random.randint(1,5)
        allocateStartList.append(table.allocate(x))
        allocateSizeList.append(x)
    print(table)
    print("-------------------删除奇数文件----------------------")
    for i in range(1,51):
        if i % 2 == 1:
            table.deallocate(allocateStartList[i-1], allocateSizeList[i-1])
    print(table)
    print("-------------------添加ABCDE文件----------------------")
    txtList = [7, 5, 2, 9, 3.5]
    blockList = []
    for txt in txtList:
        x = int(txt / 2)
        if int(txt / 2) < txt /2 :
            x = int(txt / 2) + 1
        blockList.append(x)
    letterStartList = []
    for x in blockList:
        letterStartList.append(table.allocate(x))
    print(table)
    print("-------------------ABCDE存储状态----------------------")
    print("\t起始盘块\t盘块数")
    for i in range(5):
        print(chr(65+i)+"\t"+str(letterStartList[i])+"\t\t"+str(blockList[i]))
    print("-------------------最终空闲区块表----------------------")
    print(table)
    # # 分配空闲块
    # start = table.allocate(10)
    # print('Allocated block starting at:', start)
    # print(table)
    #
    # # 再次分配空闲块
    # start2 = table.allocate(5)
    # print('Allocated block starting at:', start2)
    # print(table)
    #
    # # 归还空闲块
    # table.deallocate(start, 10)
    # print('Deallocated block starting at:', start)
    # print(table)
    #
    # # 再次归还空闲块
    # table.deallocate(start2, 5)
    # print('Deallocated block starting at:', start2)
    # print(table)
