Counts, Constant = list(map(int, input().split()))
Array = list(map(int, input().split()))
SubCount = []
# 前面的往小了改的话就得改成0，后面的往大了改就可以改很大

Min = []
Max = []

for i in range(len(Array)):
    Min.append(min(Array[i:]))
    try:
        Max.append(max(Array[:i]))
    except ValueError:      # 第一个数字前面没有数字
        Max.append(0)

for i in range(len(Min)):
    if i == len(Min)-1: break
    Count = 0 
    for j in Min[i+1:]:
        if j >= Min[i]: Count += 1
        else: break
    SubCount.append(Count)
MaxSubCount = max(SubCount)     # 获取当前最长子序列的位置
if SubCount.index(MaxSubCount)+1 <= Constant:
    Result = SubCount.index(MaxSubCount) + MaxSubCount
else:
    Result = MaxSubCount + Constant
print(Result)
