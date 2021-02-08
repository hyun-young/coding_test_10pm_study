import sys

input = sys.stdin.readline

ans_list = []
for _ in range(10):
    n = int(input())
    if (n % 42) not in ans_list:
        ans_list.append(n % 42)
#print(ans_list)
print(len(ans_list))