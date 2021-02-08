#import sys
#input = sys.stdin.readline
n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort(reverse=True) #내림차순으로 정렬
count = 0
for i in range(n):
    if k >= coin[i]:
        count += k // coin[i]
        k %= coin[i]
print(count)