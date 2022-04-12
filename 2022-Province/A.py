cards = {}
for i in range(0,10):
    cards[i] = 2021
num = 1
end = False
while not(end):
    print(num, cards)
    numstr = str(num)
    for i in numstr:
        if cards[int(i)] != 0: cards[int(i)] -= 1
        else:
            num -= 1
            end = True
    num += 1
print(num)
