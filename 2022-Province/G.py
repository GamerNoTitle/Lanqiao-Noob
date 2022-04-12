from itertools import permutations

n = int(input())
summary = 0

ls = list(range(1,n+1))
MaxPermutations = []
for i in permutations(ls):
    lesscount = 0
    for j in i:
        for k in range(i.index(j),len(i)):
            if j < i[k]: lesscount += 1
    summary += lesscount
mods = summary % 998244353
print(mods)
##    if i[0] == n: MaxPermutations.append(i)
##    else: break
##print(MaxPermutations)
