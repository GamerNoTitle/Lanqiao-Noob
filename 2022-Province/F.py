s = input()
times = 2**64
mark = 'F'*len(s)
nextS = ''
empty = False
NoOperation = True
for time in range(times):
    if s == '':
        empty = True
        break
    for i in range(len(s)):
        if i == (len(s)-1): continue    
        if s[i] == s[i+1] and s[i] != s[i-1]:   # 与右边相同与左边不同
            NoOperation = False
            mark = mark[:i-1] + 'TT' + mark[i+1:]
        elif s[i] == s[i-1] and s[i] != s[i+1]:    # 与左边相同与右边不同
            NoOperation = False
            mark = mark[:i] + 'TT' + mark[i+2:]
    if NoOperation: break
    for i in range(len(mark)):
        if mark[i] == 'F':
            nextS += s[i]
    s = nextS
    nextS = ''
    mark = 'F'*len(s)
    NoOperation = True
if empty:
    print('EMPTY')
else:
    print(s)
