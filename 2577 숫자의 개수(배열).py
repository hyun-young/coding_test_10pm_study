import sys

input = sys.stdin.readline

a, b, c = int(input()), int(input()), int(input())
ans = a*b*c # 곱셈
str_ans = str(ans) #문자열형으로 변경
ans_list = list(str(ans)) # 리스트형으로도 가능
print(str_ans)

# 리스트 또는 배열 개수 세주기
for i in range(0,10):
    print(str_ans.count(str(i)))
    # 리스트.count(해당값)으로 써도 되고,
    # 문자열형.count(해당값)으로 써도 된다.