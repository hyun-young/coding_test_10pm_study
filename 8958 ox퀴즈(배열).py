import sys

input = sys.stdin.readline
t = int(input())
check = []
for _ in range(t):
    score = 0
    correct = 0  # 개수
    check.extend(input().rstrip())
    for i in range(len(check)):
        if check[i] == 'O':
          correct += 1
          score += correct
        elif check[i] == 'X':
            correct = 0
    check.clear()
    print(score)