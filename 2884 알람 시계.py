# 시간 입력하면, 45분 빠른 시간 출력해주기

from sys import stdin

input = stdin.readline

h,m = map(int,input().split()) # 시간, 분

# 시간이 변경안되는 경우
if m >= 45:
    m -= 45
    print(h,m,sep=' ')
elif h == 0:
    h = 23
    m = 60 + (m - 45)
    print(h,m,sep=' ')
else:
    h -= 1
    m = 60 + (m - 45)
    print(h,m,sep=' ')

