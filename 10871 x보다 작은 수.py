import sys

input = sys.stdin.readline

N, X = map(int,input().split())
A = list(map(int, input().split()))
ans = []
# 출력방식 1 : list에 추가해서 출력하기
for value in A:
    if value < X:
        ans.append(value)

print(*ans) # 리스트형태가 아니라 리스트 값만 출력
# 출력방식 2 : end=' '이용하여 한줄에 붙여서 출력
for value in A:
    if value < X:
        print(value, end=' ')