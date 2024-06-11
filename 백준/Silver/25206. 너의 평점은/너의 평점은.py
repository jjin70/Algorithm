sum = 0
cnt = 0
for i in range(20):
  a,b,c = input().split()
  if c == 'A+':
    sum += float(b) * 4.5
    cnt += float(b)
  elif c == 'A0':
    sum += float(b) * 4.0
    cnt += float(b)
  elif c == 'B+':
    sum += float(b) * 3.5
    cnt += float(b)
  elif c == 'B0':
    sum += float(b) * 3.0
    cnt += float(b)
  elif c == 'C+':
    sum += float(b) * 2.5
    cnt += float(b)
  elif c == 'C0':
    sum += float(b) * 2.0
    cnt += float(b)
  elif c == 'D+':
    sum += float(b) * 1.5
    cnt += float(b)
  elif c == 'D0':
    sum += float(b) * 1.0
    cnt += float(b)
  elif c == 'F':
    sum += float(b) * 0.0
    cnt += float(b)
  else:
    pass  

print(sum/cnt)