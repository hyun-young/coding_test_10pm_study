import sys

input = sys.stdin.readline
num_list = []
# min만 쓰거나 max만 쓰는 경우는 똑같이 O(n)이다.
'''for _ in range(9):
    num_list.append(int(input()))
max_idx = 1 # 갱신이 안된다면 첫번째가 max_idx임으로
max_number = num_list[0]
for i in range(9):
    if num_list[i] > max_number:
        max_number = num_list[i]
        max_idx = i+1
#print(max_number, max_idx, sep='\n')'''
for _ in range(9):
    num_list.append(int(input()))
print(max(num_list), num_list.index(max(num_list))+1, sep='\n')