lst = []
for i in range(5):
    lst.append(input())

for i in range(15):
    for j in range(5):
        try:
            print(lst[j][i], end='')
        except:
            pass