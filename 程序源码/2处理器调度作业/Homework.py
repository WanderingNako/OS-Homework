import copy


class Homework(object):
    def __init__(self, input_time, run_time, ID):
        self.ID = ID # 进程ID
        self.input_time = input_time # 到达时间
        self.run_time = run_time # 服务时间
        self.start_time = 0 # 开始执行时间
        self.end_time = 0 # 完成时间
        self.turn_around = 0 # 周转时间
        self.dai_time = 0 # 带权周转时间
        self.state = 0  # 等待状态，未进入，已做完

    def zhouzhuan(self):
        self.turn_around = self.end_time - self.input_time
        return self.turn_around

    def daiquan(self):
        self.dai_time = round((self.end_time - self.input_time) / self.run_time, 2)
        return self.dai_time

    def output(self):
        print("%s\t\t\t%d\t\t\t%d\t\t\t%d\t\t\t%d\t\t\t%d\t\t\t    %f" % (
        self.ID, self.input_time, self.run_time, self.start_time, self.end_time, self.turn_around, self.dai_time))


def sort(Homework):
    for i in range(len(Homework) - 1):
        for j in (i + 1, len(Homework) - 1):
            if Homework[i].input_time > Homework[j].input_time:
                t = Homework[j]
                Homework[j] = Homework[i]
                Homework[i] = t


def FCFS(Homework):
    # print("FCFS:")
    # print("input_time\trun_time\tstart_time\tend_time\tturnover_time\tweighted_turnover_time\t")
    count = 0
    sort(Homework)
    num = 0
    weight_num = 0
    for i in Homework:
        if count >= i.input_time:
            i.start_time = count
        else:
            count = i.input_time
            i.start_time = count
        count += i.run_time
        i.end_time = count
        i.zhouzhuan()
        i.daiquan()
        # i.output()
        num += i.turn_around
        weight_num += i.dai_time
    average = num / len(Homework)
    weight_average = weight_num / len(Homework)
    # print("T = %f" % average)
    # print("F = %f" % weight_average)


# 寻找当前在排队的进程中要求服务时间最短的任务
def find_small(Homework):
    index = 65535
    rem = -1  # Homework 中的位置
    for i in range(len(Homework)):
        if Homework[i].state == 1 and Homework[i].run_time <= index:
            index = Homework[i].run_time
            rem = i
    return rem


def SJF(Homework):
    # print("SJF:")
    # print("input_time\trun_time\tstart_time\tend_time\tturnover_time\tweighted_turnover_time\t")
    outputList = []
    count = 0  # 时间线
    sort(Homework)
    num = 0
    weight_num = 0
    length = len(Homework)
    while len(Homework):
        for j in Homework:
            if j.input_time > count:
                j.state = 0
            else:
                j.state = 1
        if find_small(Homework) == -1:
            Homework[0].state = 1
            count = Homework[0].input_time
        small = find_small(Homework)
        Homework[small].start_time = count
        count += Homework[small].run_time
        Homework[small].end_time = count
        Homework[small].turn_around = Homework[small].zhouzhuan()
        Homework[small].dai_time = Homework[small].daiquan()
        outputList.append(copy.copy(Homework[small]))
        # Homework[small].output()
        num += Homework[small].turn_around
        weight_num += Homework[small].dai_time

        del Homework[small]
    # average = num / length
    # weight_average = weight_num / length
    # print("T = %f" % average)
    # print("F = %f" % weight_average)
    return outputList


def find_big(Homework, count):
    big_rate = -1  # 最大响应比
    index = -1
    for i in range(len(Homework)):
        rate = 1 + (count - Homework[i].input_time) / Homework[i].run_time
        if Homework[i].state == 1 and rate > big_rate:
            big_rate = rate
            index = i
    return index


def HRN(Homework):
    # print("HRN:")
    # print("input_time\trun_time\tstart_time\tend_time\tturnover_time\tweighted_turnover_time\t")
    count = 0
    length = len(Homework)
    outputList = []
    sort(Homework)
    num = 0
    weight_num = 0
    while len(Homework):
        for j in Homework:
            if j.input_time > count:
                j.state = 0
            else:
                j.state = 1
        if find_big(Homework, count) == -1:
            Homework[0].state = 1
            count = Homework[0].input_time
        big = find_big(Homework, count)
        Homework[big].start_time = count
        count += Homework[big].run_time
        Homework[big].end_time = count
        Homework[big].turn_around = Homework[big].zhouzhuan()
        Homework[big].dai_time = Homework[big].daiquan()
        outputList.append(copy.copy(Homework[big]))
        # Homework[big].output()
        num += Homework[big].turn_around
        weight_num += Homework[big].dai_time
        del Homework[big]
    # average = num / length
    # weight_average = weight_num / length
    # print("T = %f" % average)
    # print("F = %f" % weight_average)
    return outputList

def RR(Homework, quantum=1):
    outputList = []
    n = len(Homework)
    remaining_time = [h.run_time for h in Homework]  # 每个作业剩余的服务时间
    waiting_time = [0] * n  # 每个作业的等待时间
    start_time = [0] * n  # 每个作业的开始时间
    end_time = [0] * n  # 每个作业的结束时间
    turnaround_time = [0] * n  # 每个作业的周转时间
    weighted_turnaround_time = [0] * n  # 每个作业的带权周转时间
    current_time = 0  # 当前时间
    remaining_jobs = list(range(n))  # 剩余的作业列表[0, 1, 2, ..., n-1]

    # 若remaining_jobs不空
    while remaining_jobs:
        job = remaining_jobs.pop(0)
        if Homework[job].input_time > current_time:
            # 如果作业还未到达，更新当前时间
            current_time = Homework[job].input_time
        start_time[job] = current_time
        if remaining_time[job] <= quantum:
            # 如果作业在一个时间片内可以完成
            current_time += remaining_time[job]
            remaining_time[job] = 0
            end_time[job] = current_time
            turnaround_time[job] = end_time[job] - Homework[job].input_time
            weighted_turnaround_time[job] = turnaround_time[job] / Homework[job].run_time
            waiting_time[job] = turnaround_time[job] - Homework[job].run_time
        else:
            # 如果作业在一个时间片内无法完成
            current_time += quantum
            remaining_time[job] -= quantum
            end_time[job] = current_time
            remaining_jobs.append(job)
    for i in range(n):
        Homework[i].start_time = start_time[i]
        Homework[i].end_time = end_time[i]
        Homework[i].zhouzhuan()
        Homework[i].daiquan()
    # return [(start_time[i], end_time[i], turnaround_time[i], weighted_turnaround_time[i]) for i in range(n)]


if __name__ == "__main__":
    h1 = Homework(0, 4, 'A')
    h2 = Homework(1, 3, 'B')
    h3 = Homework(2, 5, 'C')
    h4 = Homework(3, 2, 'D')
    h5 = Homework(4, 4, 'E')
    h6 = Homework(20, 100, 'F')
    homework1 = [h1, h2, h3, h4, h5]
    homework2 = [h1, h3, h5, h6]
    homework3 = [h1, h2, h3, h4]
    homework4 = [h1, h3, h5, h6]
    homework5 = [h1, h2, h3, h4]
    homework6 = [h1, h3, h5, h6]
    # FCFS(homework1)
    # FCFS(homework2)
    RR(homework1)
    # SJF(homework4)
    # HRN(homework5)
    # HRN(homework6)
    for h in homework1:
        h.output()