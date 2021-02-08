#[::-1]은 뒤집어주는 것
a, b = input().split()
#type(a[::-1])  # 스트링 형태의 역순
a = int(a[::-1])
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)