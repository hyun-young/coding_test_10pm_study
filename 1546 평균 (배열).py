import sys
# boj numpy 지원안한다....
#import numpy as np

input = sys.stdin.readline

n = int(input())
score_list = list(map(int, input().split()))
m = max(score_list)
for i in range(len(score_list)):
    score_list[i] = score_list[i]/m * 100
print(round(sum(score_list) / n, 6))

# numpy 쓴 코드
'''import numpy as np

input = sys.stdin.readline

n = int(input())
score_list = list(map(int, input().split()))
#print(score_list)
m = max(score_list)
new = np.array(score_list)/m * 100
print(round(sum(new) / n, 6))'''