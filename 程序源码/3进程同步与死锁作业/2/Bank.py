def bank(start, request):
    available = ['2', '3', '3']#资源向量
    proc = ['P1', 'P2', 'P3', 'P4', 'P5']#进程
    allocation = ['2', '1', '2', '4', '0', '2', '4', '0', '5', '2', '0', '4', '3', '1', '4']#分配矩阵
    max_ = ['5', '5', '9', '5', '3', '6', '4', '0', '11', '4', '2', '5', '4', '2', '4']#最大需求矩阵
    need = []#需求矩阵
    work = []#工作向量
    finish = []
    wpa = []#work+allocation
    n = len(available)#资源数目
    for i in range(len(max_)):
        need.append(eval(max_[i]) - eval(allocation[i]))#计算need
    # print("从",proc,"中选择一个请求进程",end=":")
    # start = input()
    # print(start)
    # print("输入请求的资源(共{a}个，以空格区分)".format(a=n),end=":")
    # request_t = input()
    # request = request_t.split(" ")
    # print(request)
    index = 0
    for i in range(len(proc)):
        if start == proc[i]:
            index = i
            break
    flag = False
    for i in range(n):
        if eval(request[i]) > need[i+index*n]:#步骤1判断
            flag = False
            break
        else:
            flag = True
            continue
    if flag == True:
        for i in range(n):
            if eval(request[i]) > eval(available[i]):#步骤2判断
                flag = False
                break
            else:
                flag = True
                continue
    if flag == True:
        for i in range(n):#步骤3修改资源
            available[i] = eval(available[i]) - eval(request[i])
            allocation[i+index*n] = eval(allocation[i+index*n]) + eval(request[i])
            need[i+index*n] = need[i+index*n] - eval(request[i])
        work = available
        work_str = [0]*n*len(proc)
        finish = [False]*len(proc)
        for i in range(len(allocation)):
            allocation[i] = str(allocation[i])
            allocation[i] = eval(allocation[i])
        queue = []#安全序列
        for i in range(len(proc)):#安全性检查
            for index_t in range(len(proc)):
                if index_t not in queue:
                    if finish[index_t] == False:
                        flag_t = True
                        for j in range(n):
                            if need[j+index_t*n] > work[j]:#判断need[i][j]≤work[j]
                                flag_t = False
                                break
                        if flag_t == True:
                            for j in range(n):
                                work_str[j+index_t*n] = work[j]
                                work[j] = work[j] + allocation[j+index_t*n]
                            queue.append(index_t)
                            finish[index_t] = True
        for i in finish:
            if i == False:
                flag = False
                break
        for i in range(len(work_str)):
            wpa.append(work_str[i]+allocation[i])
        if flag == True:
            # with open("yhj_res.txt","w",encoding="utf-8") as ff:
            #     ff.write("\t进程\twork\tallocation\tneed\twork+allocation\tfinish\n")
            #     res_list = []
            #     for i in queue:
            #         ff.write("\t"+str(proc[i]))
            #         ff.write("\t"+str(work_str[i*n:i*n+n]))
            #         ff.write("\t"+str(allocation[i*n:i*n+n]))
            #         ff.write("\t"+str(need[i*n:i*n+n]))
            #         ff.write("\t"+str(wpa[i*n:i*n+n]))
            #         ff.write("\t   "+str(finish[i])+"\n")
            #         res_list.append(proc[i])
            #     ff.write("可以分配，存在安全序列"+str(res_list))
            #     print("可以分配，存在安全序列"+str(res_list))
            res_list = []
            for i in queue:
                res_list.append(proc[i])
            return str(res_list)
        else:
            # with open("yhj_res.txt","w",encoding="utf-8") as ff:
            #     ff.write("无法分配")
            #     print("无法分配")
            return None
        # ff.close()


if __name__ == '__main__':
    start = 'P2'
    request = ['100', '1', '0']
    print(bank(start,request))