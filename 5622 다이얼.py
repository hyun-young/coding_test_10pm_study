# 다이얼 전화기

S = input().strip()
ans = 0
dictionary = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

for i in range(len(S)):
    for dial in dictionary:
        if S[i] in dial:
            ans += (dictionary.index(dial) + 3)
print(ans)
