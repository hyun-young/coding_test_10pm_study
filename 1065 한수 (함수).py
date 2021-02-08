import sys

n = int(sys.stdin.readline())
h_list = []
# 10은 한수, 1은 한수, 2도 한수, 3도 한수
cnt = 0

def hansoo(k):
    num_list = list(str(k))
    if len(num_list) <= 2:
        return k
    else:
        for i in range(len(num_list)-2):
            if (int(num_list[i]) + int(num_list[i+2])) != 2*int(num_list[i+1]):
                return -k
        return k


for k in range(1,n+1):
    h_list.append(hansoo(k))
    if h_list[k-1] > 0:
        cnt += 1
print(cnt)

