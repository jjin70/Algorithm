def solution(s):
    cnt = 0 
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        elif s[i] == ')':
            if cnt == 0:
                return False
            cnt -= 1 
    return cnt == 0

n = int(input())
for i in range(n):
  m = input()
  if solution(m) == True:
    print("YES")
  else:
    print("NO")