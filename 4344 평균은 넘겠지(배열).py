import sys

input = sys.stdin.readline

c = int(input())

for _ in range(c):
    score = list(map(int,input().split()))
    n = score.pop(0)
    avg = sum(score) / n
    cnt = 0 # 평균 넘는 학생 수
    for i in range(n):
        if score[i] > avg:
            cnt += 1
    score.clear()
    print('%2.3f%%'%(cnt/n*100)) # 자릿수 출력방법 확인하기 , f''랑 '{}'.format은? 모르겠음
