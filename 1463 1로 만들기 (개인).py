import sys

input = sys.stdin.readline

n=int(input())
cnt = 0
while 1:
    if n % 3 == 0:
        n //= 3
        cnt += 1
    if n % 2 == 0:
        n //= 2
        cnt += 1
    else:
        n -= 1
        cnt += 1
    if n == 1:
        break
print(cnt)