maxnum = int(input())
pos = int(input())

def summary(num):
    length = len(str(num))
    s = 0
    for i in str(num):
        s += int(i)
    return s
nums = []
for i in range(1,maxnum+1):
    nums.append((i,summary(i)))
nums.sort(key=lambda s: s[0])
nums.sort(key=lambda s: s[1])
print(nums[pos-1][0])

