import sys
input = sys.stdin.readline

n = int(input())
word_list=[]
for _ in range(n):
    word_list.append(str(input()))
alpabet = [0 for i in range(26)] # 0 26개 알파벳

alpha_dic = {}
for word in word_list: # 단어리스트의 단어들에 대해(n번))
    cnt = 0
    for i in word: #단어알파벳수만큼
        if i not in alpha_dic:
            alpha_dic[i] = 10 ** (len(word) - cnt -1)
        elif i in alpha_dic:
            alpha_dic[i] += 10 **(len(word)- cnt - 1)
        cnt += 1
print(alpha_dic)