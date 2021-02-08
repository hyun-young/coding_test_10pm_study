import sys
input = sys.stdin.readline

cnt = 1 # count
a, b = map(int, input().split())

while True:
    if b == a:
        break
    elif (b % 2 == 1 and b % 10 != 1) or b < a:
        cnt = -1
        break
    elif b % 10 == 1:
        b = (b - 1) // 10
        cnt += 1
        continue #?
    else:
        b //= 2
        cnt += 1
        continue #?
print(cnt)



#for in range
   # A = 10* A + 1
    #A *= 2
    #if A == B:
