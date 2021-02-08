import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    a,b = map(int,input().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')
    # f'{변수이름}'으로 출력하면 깔끔