N = int(input())
data = list(map(int, input().split()))
cal = list(map(int, input().split()))
max_ans = -1000000000
min_ans = 1000000000


def dfs(idx, ans):
    global max_ans, min_ans

    if idx == N:
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)
        return

    if cal[0] > 0:
        cal[0] -= 1
        dfs(idx + 1, ans + data[idx])
        cal[0] += 1
    if cal[1] > 0:
        cal[1] -= 1
        dfs(idx + 1, ans - data[idx])
        cal[1] += 1
    if cal[2] > 0:
        cal[2] -= 1
        dfs(idx + 1, ans * data[idx])
        cal[2] += 1
    if cal[3] > 0:
        cal[3] -= 1
        dfs(idx + 1, ans // data[idx])
        cal[3] += 1


dfs(1, data[0])
print(max_ans)
print(min_ans)
