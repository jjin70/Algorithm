n, b = map(int, input().split())
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

r = ''
while n!=0:
    r += str(num[n % b])
    n = n // b

for i in range(len(r)-1, -1, -1):
    print(r[i], end='')