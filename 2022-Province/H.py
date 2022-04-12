from math import ceil
TotalATK = 0
SkillCounts, UpgradeTimes = list(map(int, input().split(' ')))
Skills = []
for i in range(SkillCounts):
    ATK, PointMinus = list(map(int, input().split(' ')))
    MaxUpgradeTimes = ceil(ATK/PointMinus)
    Skills.append([ATK, PointMinus, MaxUpgradeTimes])

Skills.sort(key=lambda s: s[0],reverse=True)

for i in range(UpgradeTimes):
    TotalATK += Skills[0][0]
    Skills[0][0] -= Skills[0][1]    # ATK减少固定值
    Skills[0][2] -= 1   # 可升级次数-1
    Skills.sort(key=lambda s: s[0],reverse=True)
print(TotalATK)
