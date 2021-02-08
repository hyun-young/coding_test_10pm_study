import sys

n = sys.stdin.readline().rstrip()
# rstrip() 없으면 틀림
# sys.stdin.readline()은 끝의 개행 문자를 포함하기 때문
# ord는 문자를 입력하면 아스키코드 return
# chr은 아스키코드 입력시 해당 문자 return
print(ord(n))



