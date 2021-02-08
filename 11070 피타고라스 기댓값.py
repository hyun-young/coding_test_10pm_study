import sys

input = sys.stdin.readline


T = int(input()) # test 개수
ans = []

for t in range(T):
    # 테스트 마다 n ,m, matrix 초기화
    n, m = map(int, input().split())
    score_matrix = [[0]*2 for _ in range(n)] # 득점, 실점
    for _ in range(m): #matrix 만들기
        a, b, p, q = map(int,input().split())
        # 같은 팀끼리 여러번 경기할 수도 있음
        score_matrix[a-1][0] += p
        score_matrix[a-1][1] += q
        score_matrix[b-1][0] += q
        score_matrix[b-1][1] += p
        #print(score_matrix)
    pythagorean = []
    for i in range(n): # 득점 실점
        S = score_matrix[i][0] # 득점
        A = score_matrix[i][1] # 실점
        if S == 0 and A == 0: #실수: (S and A) == 0
            pythagorean.append(0) # 실수: print(0)
        else:
            pythagorean.append(S ** 2 / (S ** 2 + A ** 2))
        # print(pythagorean)
        print(int(max(pythagorean) * 1000))
        print(int(min(pythagorean) * 1000))
    #pythagorean.clear()
#for a in range(len(ans)):
 #   print(ans[a])




