line = 1189
col = 841
size = input()
times = int(size[1:])
print(times)
for i in range(times):
    if line >= col: line = line // 2
    else: col = col // 2
print(max([line,col]))
print(min([line,col]))
