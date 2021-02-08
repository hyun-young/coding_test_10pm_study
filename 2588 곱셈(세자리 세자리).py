# 2588 곱셈

# 세자리 세자리 곱의 형태를 출력

a = int(input())
b = int(input())
# b를 자릿수로 표현하기
ans = a*b
num_b=[]
for _ in range(3):
    tmp = b % 10
    b //= 10
    num_b.append(tmp)
for i in range(3):
    print(a*num_b[i]) #3,4,5

print(ans) #6
