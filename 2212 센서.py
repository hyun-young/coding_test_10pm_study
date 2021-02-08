import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
spot = sorted(list(map(int, input().split())))
# k는 구역,분할을 의미 : k=2면 2구역,1분할으로 생각
# 최솟값이 되려면 분할 지역은 가장 거리가 긴 곳이어야함
# 분할이 된다면 거리 계산을 하지 않기 때문에
#
# #집중국이 많으면 결과는 x
if k >= n :
    print(0)
else:
    print(spot)
    gap = []
    for i in range(1,n): # i-1이용위해 1부터
        gap.append(spot[i]-spot[i-1])# 거리계산
    gap.sort(reverse = True)

    #거리순으로 정렬(큰 거리 분할하기 위해)
    print(gap)
    for _ in range(k-1):
        gap.pop(0)
    print(sum(gap))