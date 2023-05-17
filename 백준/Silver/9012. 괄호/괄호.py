n = int(input())
for i in range(n):
  lst = []
  cnt = 0
  m = input()
  for j in m:
    if j=='(':
      lst.append(j)
      cnt+=1
    else:
      if cnt>0:
        cnt-=1
      else:
        print("NO")
        break
  else:
    if cnt==0:
      print("YES")
    else:
      print("NO")
    