n = int(input())
num_list = list(map(int,input().rstrip()))
ans = 0
for i in range(len(num_list)):
    ans += num_list[i]
print(ans)