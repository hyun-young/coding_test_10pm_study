# 문자열 s에서 단어만 뒤집기(태그는 그대로)
# 1. 알파벳 소문자,숫자,공백,특수문자<,>만 쓴다
# 2. 문자열 시작과 끝은 공백이 될 수 없다.
# 3. <>가 문자열에 있는 경우는 선<,(알파벳,공백만 옴) 후>
# 4. 태그는 <>로 끝나는 길이가 3 이상인 부분 문자열
# 5. 단어는 알파벳,숫자로 이루어짐, 공백으로 단어 구분
# 6. 태그는 단어가 아님, 태그와 단어 사이엔 공백 없음

# 1.   '<' 있을 경우는 일렬로 저장하기 때문에 정답 문자열에 그대로 입력
# 1-1) '<' 받았을 경우 flag =1로 변경 후 그대로 정답에 저장
# 1-2) '>' 만났을 경우 flag =0으로 변경
# 2.   그외의 경우 공백 혹은 '<'를 만날 경우까지 저장 후 뒤집을 문자열이다
# 2-1) 그래서 그 전까지 ans 배열에 저장 후 [::-1] 활용하여 뒤집고 문자열에 넣음
# 2-2) 공백의 경우 누락돼서 뒤집고 문자열연산 후 넣음
# 2-3) 마지막 단어를 뒤집어야 할 경우 대비하여 끝에 ans배열에 저장 여부 확인
import sys
input = sys.stdin.readline

S = input().rstrip()
ans = []
flag = False ### 괄호 상태
result = ''
for char in S:
    if char == '<':
        if len(ans) != 0:  # 괄호 안이고, ans에 들어있는 경우
            ans = ans[::-1] # 거꾸로 넣기
            for i in range(len(ans)):
                result += ans[i]
            ans.clear() # 다 넣었으면 비워주기
        flag = True     #괄호 안임을 의미
        result += char
    elif flag:          # 괄호 안 상태였다면
        result += char  # 괄호안에 그대로 넣어주기
        if char == '>': # 괄호 안 상태였다면
            flag = False  #괄호 밖 상황으로
    elif char == ' ':
        ans = ans[::-1] #거꾸로 넣어주기
        for i in range(len(ans)):
            result += ans[i]
        ans.clear()
        result += char
    else:
        ans.append(char)

if len(ans) != 0: # 아직 ans에 남아있다면
    ans = ans[::-1] #거꾸로 넣어주고
    for i in range(len(ans)):
        result += ans[i]
    ans.clear()
print(result)


