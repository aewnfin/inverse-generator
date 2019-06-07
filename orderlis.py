#orderList=input("一组规律数字的序列")

#函数 ‘equalInList（）’判断 参数：序列 内元素是否全部相同
'''def equalInList(numList):
    No1=numList[0]
    for i in numList:
        if No1!=i:
            No1=i
            break
    if No1==numList[0]:
        return True
    else:
        return False'''

#函数 ‘orderNext_getTile（）’ 判断 参数：序列 内元素是否重复排列,重复排布则返回重复序列
def orderNext_getTile(linkList):

    listLen=len(linkList)
    harftLen=listLen//2
    #print(f"{harftLen}")
    for i in range(1,harftLen+1):
        part= linkList[0:i]
        #print(f"标准：{part}")#
        tern=int(listLen/i)
        #print(f"次数{tern}")#
        last=listLen-tern*i
        #print(f"剩余{last}")#
        leave= linkList[i * tern:]
        #print(f"余下{leave}")#
        snos=True
        for j in range(1,tern):
            start=i*j
            #print(f"起始点位序列，起始点位置{start}")
            if part!= linkList[start:start+i]:
                #print(f"因为{part}！={numlist[start:start+i]}")
                snos=False
                break
        for o in range(0,last):
            if part[o]!=leave[o]:
                snos=False
                #print(f"不等{part[o]},{leave[o]}")
                break
        #print(snos)
        if snos:
            return part
    return False

#生成器 ‘orderNext_reTile（）’ 参数：序列 无限重复输入的序列
def orderNext_reTile(tileList):
    long=len(tileList)
    i=0
    while True:
        yield tileList[i]
        i+=1
        if i >=long:
            i=0

#函数 ‘getNext_fromLinear（）’ 参数：需要规律生成的数字序列 返回规律序列的生成器/无规律序列返回False
def getNext_fromLinear(numList):

    le_s = []
    le_n = []

    for i in numList:
        if i >= 0:
            le_s.append('+')
            le_n.append(i)
        elif i < 0:
            le_s.append('-')
            le_n.append(-i)
        else:
            return False

    elfs = orderNext_getTile(le_s)
    elfn = orderNext_getTile(le_n)

    if elfn != False and elfs != False:
        def foNext():
            nlis=orderNext_reTile(elfn)
            slis=orderNext_reTile(elfs)
            while True:
                n=next(nlis)
                s=next(slis)
                if s=='-':
                    num=-n
                else:
                    num=n
                nextNum=num
                yield nextNum
        return foNext
    elif elfn == False and elfs != False:
        le_nn=[]
        for i in range(0,len(le_n)-1):
            le_nn.append(le_n[i+1]-le_n[i])
        if le_nn !=[]:
            yel=getNext_fromLinear(le_nn)
            if yel != False:
                def ffnext():
                    start = le_n[0]
                    a=yel()
                    fsl = orderNext_reTile(elfs)
                    while True:
                        fsl_s = next(fsl)
                        if fsl_s == '-':
                            renn = -start
                        else:
                            renn = start
                        yield renn
                        yel_n = next(a)
                        start += yel_n
                return ffnext
            else:
                return False
        else:
            return False
    else:
        return False

'''**************
输入
'''
#lf=[1,3,6,10,15]
#lf=[1,2,3,4]
#lf=[-1,2,-3,4]
#lf=[1,3,5,7,9]
#lf=[6,8,10]
#lf=[7,8,6,9,5,10,4]
#lf=[1,22,333,4444,55555]#false
lf=[11,22,33,44]
'''for n in orderNext_reTile(lf):
    print(n)
    i+=1
    if i== 10:
        break'''

'''a=orderNext_reTile(lf)
while True:
    print(next(a))
    i += 1
    if i == 10:
        break'''
'''*****************
输出
'''
af=getNext_fromLinear(lf)

'''*****************
验证输出
'''
terns=20 #生成长度
if af ==False:
    print("False")
else:
    yelist=af()#运行生成器
    for i in range(terns):
        print(next(yelist))
