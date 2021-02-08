# 다시 그 글자 쓰면 그룹단어가 아님!

n = int(input())
cnt = 0
for _ in range(n):
    flag = True
    result = []
    word = input()
    for alpha in word:
        if len(result) == 0:
            result.append(alpha)
        # 들어있지 않거나, 들어있는데 가장 최근꺼랑 같다면 true임
        elif alpha not in result or alpha == result[-1]:
            result.append(alpha)
            #print('2',alpha)
        else:
            #print(alpha, 'now false')
            flag = False
    #print(flag)
    if flag: # 그룹단어일때만 숫자세주기
        cnt += 1
print(cnt)