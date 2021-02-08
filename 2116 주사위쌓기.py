import sys

input = sys.stdin.readline

# 주사위는 1- 6까지 하나씩 있음
# 붙어있는 면의 주사위 숫자가 같아야함
# 1번 주사위는 마음대로 놓을 수 있음
# 사각기둥이 되는 주사위탑의 4개의 옆면
# 옆면의 어느 한면의 숫자합 최대가 되도록
n = int(input())
dice = []

for _ in range(n):
    dice.append(list(map(int,input().split())))

# 반대편 index
opp_list = [5,3,4,1,2,0]
ans = 0
for i in range(6):
        result = []
        number = [1, 2, 3, 4, 5, 6]
        # 짝지어 제거해 result에 추가
        number.remove(dice[0][i])
        side = dice[0][opp_list[i]]
        number.remove(side)
        result.append(max(number)) # 최대한 6이 많이 들어가도록!
        for j in range(1,n):
            number = [1, 2, 3, 4, 5, 6]
            number.remove(side)
            # 그 다음 조합 확인
            side = dice[j][opp_list[dice[j].index(side)]]
            number.remove(side)
            result.append(max(number))
        if ans < sum(result):
            ans = sum(result)
print(ans)