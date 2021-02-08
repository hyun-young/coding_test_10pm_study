import sys

input = sys.stdin.readline

S = input()
print(S)
a_flag = False # 소괄호가 아닌 상태 ()
b_flag = False # 대괄호가 아닌 상태 []
number = []
# 기호 숫자로 바꿔주기
for char in S:
    if char == '(':
        number.append(0)
    elif char == '[':
        number.append(1)
    elif char == ']':
        number.append(2)
    elif char ==')':
        number.append(3)
print(number)

ans=[]
#result = []
# print 0 출력인 경우
for i in (1, len(number)):
    if number[i] - number[i - 1] == 2:
        print(0)
        break
    print('통과~')
    #while number[i] - number[i-1] == 3 or 1:

    #if number[i] - number[i-1] == 3:
     #       ans.append(2)

#for char in S: #char=괄호
 #   if char == '(':
  #      if a_flag:
