def solution(s):
    while '()' in s:
        sp = s.split('()') 
        s = ''.join(sp) 
    return len(s) == 0 

n = int(input())
for i in range(n):
  m = input()
  if solution(m) == True:
    print("YES")
  else:
    print("NO")