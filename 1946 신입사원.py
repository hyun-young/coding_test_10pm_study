import sys
import heapq
input = sys.stdin.readline

# 필기 1등, 실기 1등 기준으로 순위 만족하는 애들만 뽑기

t = int(input())
for i in range(t):
    n = int(input()) # 지원자 숫자
    rank = []
    for i in range(n):
        a, b = map(int, input().split())
        heapq.heappush(rank,(a,b))
    rank.sort() #(면접 1등이 맨앞으로)
    # 신입사원 출력
    cnt = 0
    standard = n # 기준
    for f, s in rank: #first, second
        if s == 1: # 실기 1등이면 종료
            cnt += 1
            break
        elif s <= standard: # 처음이 기준이 되도록
            cnt += 1
            standard = s # 면접1등이 기준이 되도록 second 기준 갱신
    print(cnt)
