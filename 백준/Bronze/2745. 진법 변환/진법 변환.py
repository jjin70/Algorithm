n, b = input().split() 
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
ans = 0
n = n[::-1]
for i in range(len(n)):
    sum = num.index(n[i])*(int(b)**i)
    ans += sum
print(ans)