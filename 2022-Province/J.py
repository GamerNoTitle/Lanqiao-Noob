Length, Constant = list(map(int, input().split(' ')))   # 获得数列长度以及连续的数字的数量K
Array = list(map(int, input().split(' ')))  # 构造输入的数列
MinusTimes = []

##def GetConstantArray(array):
##    ConstantPosList = []
##    for i in range(len(array)):
##        if i == len(array)-1: break
##        if array[i]+1 == array[i]:
##            StartPos = i
##            CusPos = i+1
##            EndPos = i+1
##            while 1:
##                if CurPos+1 >= len(array):        # 指针已经指向最后一个数字了
##                    ConstantPosList.append((StartPos, EndPos))      # 将位置信息存储进入列表中，终止循环
##                    break                    
##                if array[CurPos+1] == array[CurPos]+1: CurPos += 1      # 当指针指向的下一个数字与当前指向的数字+1相等就继续
##                else:   # 指针指向的下一个数字与当前数字+1不相等
##                    ConstantPosList.append((StartPos, EndPos))      # 将位置信息存储进入列表中，终止循环
##                    break
##    return ConstantPosList
##print(GetConstantArray(Array))

for i in range(Length):
    if i+Constant >= Length+1: break
    MinusTimes.append(max(Array[i:i+Constant]))

MaxMinusTimes = max(MinusTimes)
MaxMinusTimesPos = MinusTimes.index(MaxMinusTimes)
MinusTimesSum = []
for i in range(Constant):
    try:
        MinusTimesSum.append(sum(MinusTimes[MaxMinusTimesPos-i:MaxMinusTimes+i]))
    except:
        MinusTimesSum.append(sum(MinusTimes[MaxMinusTimesPos-i:]))
MaxMinusTimesSumPos = MinusTimesSum.index(max(MinusTimesSum))    # 确定从哪里开始减，怎么减
