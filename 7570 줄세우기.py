import sys

##?? 최장수열?
#LIS 응용
# 움직인 사람들의 총 수가 최소
# 움직이지 않은 사람들의 수가 최대가 된다
input = sys.stdin.readline
child = int(input())
order = list(map(int, input().split()))
order.insert(0, 0) # 인덱스 맞춰주기 위해
stack = deque()

dp = [0] * (n+1) # dp의 최솟값은 0
order.insert(0,0) # 0이 있어야 dp에 값 나타낼 수 있음
sub = []
for i in range(1, len(order)):
    for j in range(i): # i를 기준으로 그 전 값들 비교
        if order[i] > order[j]: # 이 조건을 만족하면 dp가 증가
            dp[i] = max(dp[i],num_list[i]+dp[j]) # max값을 쓴이유는 자기자신 이전에 모든 값들과 비교했을 때 가장 큰 경우를 써야하므로



