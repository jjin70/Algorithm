import sys
input=sys.stdin.readline

n = int(input())
lst =[]

for i in range(n):
    m = int(input())
    if m == 0:
        lst.pop()
    else:
        lst.append(m)
print(sum(lst))