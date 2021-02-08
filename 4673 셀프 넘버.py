import sys

input = sys.stdin.readline

# n과 n의 각 자리수를 더하는 함수
k_list=[]
def kaprekar(n):
    ans = 0
    for value in list(str(n)):
        ans += int(value) # value의 자릿수 더하기
    return n + ans

for i in range(1,10001):
    k_list.append(kaprekar(i))

for self_num in range(1,10001):
    if self_num in k_list:
        pass
    else:
        print(self_num)