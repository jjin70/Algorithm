import sys
input=sys.stdin.readline

n = int(input())
lst = []
i = 0
for i in range(n):
    s = input().split()

    if s[0] == 'push':
        lst.append(s[1])
    elif s[0]=='pop':
        if len(lst) == 0:
            print(-1) 
        else: 
            print(lst.pop())
    elif s[0]=='empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif s[0]=='size':
        print(len(lst))
    elif s[0]=='top':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1]) 
    