from PyQt5.QtWidgets import QTabWidget,QTableWidgetItem
import multiprocessing as mp
import time
import random


# 生产者函数
def producer(queue, empty, full):
    # while True:
        # 随机生成一个产品
        item = random.randint(1, 100)
        # 请求一个空槽位
        empty.acquire()
        # 将产品放入队列
        queue.append(item)
        print(f"生产者生产了产品 {item}")
        with open("output.txt", "a", encoding="UTF-8") as f:
            f.write(f"生产者生产了产品 {item}\n")
        # 释放一个满槽位
        full.release()
        # 随机等待一段时间
        time.sleep(random.random())

# 消费者函数
def consumer(queue, empty, full):
    # while True:
        # 请求一个满槽位
        full.acquire()
        # 从队列中获取一个产品
        item = queue.pop(0)
        print(f"消费者消费了产品 {item}")
        with open("output.txt", "a", encoding="UTF-8") as f:
            f.write(f"消费者消费了产品 {item}\n")
        # 释放一个空槽位
        empty.release()
        # 随机等待一段时间
        time.sleep(random.random())

if __name__ == "__main__":
    # 创建共享队列
    q = mp.Manager().list()
    # 创建信号量
    empty = mp.Semaphore(10)
    full = mp.Semaphore(0)
    num_processes = 5
    processes = []
    for i in range(num_processes):
        processes.append(mp.Process(target=producer, args=(q, empty, full)))
        processes.append(mp.Process(target=consumer, args=(q, empty, full)))

    # 启动所有进程
    for p in processes:
        p.start()

    # 等待所有进程结束
    for p in processes:
        p.join()