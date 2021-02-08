import sys

# 2438
input = sys.stdin.readline

n = int(input())
star ='*'
for i in range(1,n+1):
    ans = star * i
    print(ans)

# 2439

input = sys.stdin.readline

n = int(input())
star ='*'
for i in range(1,n+1):
    ans = star * i
    print(f'{ans:>{n}}') # ':>'--n만큼 오른쪽으로 ans를 받는다는 의미
