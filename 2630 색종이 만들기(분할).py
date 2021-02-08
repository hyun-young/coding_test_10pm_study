import sys

input = sys.stdin.readline

# 4분할 해주기
def cutting(a,b,n): #a,b는 좌표
    global blue_cnt
    global white_cnt
    color = paper[a][b] #0 또는 1로 시작
    for i in range(a, a + n):
        for j in range(b, b + n):
            if color != paper[i][j]:
                #통일이 아니라면 사등분
                # 4등분 시작
                n //= 2
                cutting(a,b,n) #1
                cutting(a,b+n,n)#2
                cutting(a+n,b,n)#3
                cutting(a+n,b+n,n)#4
                return
    if color == 0:
        white_cnt += 1
        return
    elif color == 1:
        blue_cnt += 1
        return

n = int(input()) # 2의 제곱수 1<=n<=128
paper = [(list(map(int,input().split())))for _ in range(n)]
white_cnt = 0
blue_cnt = 0
cutting(0,0,n) # 첫좌표는 0,0부터 시작
print(white_cnt)
print(blue_cnt)