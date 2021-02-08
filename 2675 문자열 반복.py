T = int(input())
for _ in range(T):
    R,S = input().split()
    R = int(R)
    S = str(S)
    text ="" # 그대로 붙이고 싶으면 문자열 형식을 곱해라
    for i in range(len(S)):
        text += S[i] * R
        '''print(S[i] * R, end='')''' # 이 방법도 유효
    #print(*ans) 공백발생!!, 리스트로 받아서 출력하는 문제가 아님
    print(text)