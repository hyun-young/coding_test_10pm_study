# 10952 (0 0 들어오면 종료)

'''ans = 1 # while문 진입을 위해
while ans: # ans가 0이 된다면 다음 반복 진행 x
    a, b = map(int,input().split())
    ans = a + b
    if ans != 0: # 0은 출력하지 않음
        print(ans)'''

# 10951 (입력이 끝나면 종료)
# 끝나는 조건을 만들어줘야함 !! try - except
# 몇개를 받을지 모르는 상태에서 입력을 받을때는
# sys와 try,except 사용!!
# 예외처리!!
import sys

# input으로만 받을 때
'''while 1: # 특별한 종료조건이 없음
    try:
        a, b = map(int,input().split())
        print(a+b)
    except EOFError: # EOFError일 때
        break
# input을 sys.stdin.readline으로 받으면
# sys--는 비어있는 거 까지 값으로 인지함
while 1: # 특별한 종료조건이 없음
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except: # ValueError일 때(비워줘도 됨)
        break'''

# 1110 더하기 사이클
#55 - 50 - 05 - 55
#2'6' - '6'"8" - "8"'4' - '4'"2" - "2"6 # 4번

n = int(input())
cnt = 0
new = n
dig_10 = n // 10
dig_1 = n % 10
while 1:
    new = 10*(dig_1) + ((dig_10 + dig_1) % 10)
    dig_1 = new % 10
    dig_10 = new // 10
    cnt += 1
    if n == new:
        break
print(cnt)