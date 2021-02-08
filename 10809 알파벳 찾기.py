S = list(map(str, input()))
arr = [-1] * 26
alphabet = list(map(chr,range(97,123)))#알파벳 소문자 아스키코드
for i in range(len(S)):
    # S단어의 글자가 알파벳 인덱스로 몇인지 idx에 저장
    idx = alphabet.index(S[i])
    if arr[idx] == -1: #아직 업데이트 안된 거라면
        arr[idx] = i

for j in arr:
    print(j,end=' ')