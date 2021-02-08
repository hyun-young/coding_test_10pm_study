# 11053

import sys

input = sys.stdin.readline

# 최장증가부분수열(LIS)
# 수열에서 오름차순으로 정렬된 가장 긴 부분 수열
# 즉, 새로운 오름차순 부분수열의 길이를 최대로 하는 것
# ex) 1 6 2 5 7 3 5 6 이면
# '1' 6 '2' 5 7 '3' '5' '6' == 1 2 3 5 6
# ex) 4 1 2 5 7 3 5 6 이면
# 1 2 3 5 6이 정답
# 수열이 주어지면 가장 긴 증가하는 부분 수열을 구하는 프로그램
# 푸는 방법 2가지
# 1. o(n^2)
# 새로운 배열 dp[i]: num_list[i]를 마지막 값으로 가지는 가장 긴 길이
# num_list[i]가 증가부분수열의 마지막 값이되려면 num_list[i]가 추가되기 전
# 증가부분수열의 마지막 값이 num_list[i]보다 작아야 한다.(그래야 추가하겠지)
# 따라서, num_list[i]가 추가 될 수 있는 증가부분수열의 최대길이에 1을 더한 값


'''n = int(input())
num_list = list(map(int,input().split()))
dp = [0] * (n+1) # dp의 최솟값은 0
num_list.insert(0,0) # 0이 있어야 dp에 값 나타낼 수 있음
for i in range(1, len(num_list)):
    for j in range(i): # i를 기준으로 그 전 값들 비교
        if num_list[i] > num_list[j]: # 이 조건을 만족하면 dp가 증가
            dp[i] = max(dp[i],dp[j]+1) # max값을 쓴이유는 자기자신 이전에 모든 값들과 비교했을 때 가장 큰 경우를 써야하므로
        # 비교해보기
print(num_list)
print(dp)
print(max(dp))'''

# 11055
n = int(input())
num_list = list(map(int,input().split()))
dp = [0] * (n+1) # dp의 최솟값은 0
num_list.insert(0,0) # 0이 있어야 dp에 값 나타낼 수 있음
sub = []
for i in range(1, len(num_list)):
    for j in range(i): # i를 기준으로 그 전 값들 비교
        if num_list[i] > num_list[j]: # 이 조건을 만족하면 dp가 증가
            dp[i] = max(dp[i],num_list[i]+dp[j]) # max값을 쓴이유는 자기자신 이전에 모든 값들과 비교했을 때 가장 큰 경우를 써야하므로


        # 비교해보기
print(num_list)
print(dp)
print(max(dp))
