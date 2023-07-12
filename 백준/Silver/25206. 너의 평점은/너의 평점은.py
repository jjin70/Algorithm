sum = 0
credit = 0 

for i in range(20):
    a, b, c = map(str, input().split())
    if c != 'P':
        credit += float(b)
        if c == 'A+':
            score = 4.5
        elif c == 'A0':
            score = 4.0
        elif c == 'B+':
            score = 3.5
        elif c == 'B0':
            score = 3.0
        elif c == 'C+':
            score = 2.5
        elif c == 'C0':
            score = 2.0
        elif c == 'D+':
            score = 1.5
        elif c == 'D0':
            score = 1.0
        elif c == 'F':
            score = 0
        sum += float(b) * score

print(sum/credit)