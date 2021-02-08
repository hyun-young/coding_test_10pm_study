n = int(input())

integer = list(map(int,input().split()))
# min,max함수
#print(min(integer),max(integer),sep=' ')
#print(f'{min(integer)}{max(integer)}') 도 ㅇㅋ
# for문으로 min,max찾아보기
max_num = integer[0]
min_num = integer[0]
for value in integer:
    if value > max_num: #원래값보다 큰수가 나타났을때
        max_num = value # 갱신
    if value < min_num: #원래값보다 작은수가 나타났을때
        min_num = value # 갱신
print(min_num, max_num)