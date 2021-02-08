
# 다시해보기
word = input().upper()
# set으로 리스트 만들어서 확인해보기
word_list = list(set(word))
result = []



#count함수
# 리스트.count(숫자세려는인자) for문을 돌려 확인
for alpha in word_list: # set으로 받지 않으면 result에 중복됨
    result.append(word.count(alpha))
# set으로 받은거라서 어떤 알파벳인지 확인할 수 없음
print(result)
# 다만 set도 한번 지정한거라 순서는 없지만
# 순서가 랜덤일 뿐이지 매번 index가 random인 것은 아님
# ex) set에 q,a,g,f,k 순으로 저장된다면(랜덤)
# 그 set의 인덱스는 q,a,g,f,k순으로 고정된다는 의미
# 따라서 매번 random인 것은 아님!!(이미저장)




# 우리가 원하는 index 저장
# if - else문 안쓴다면?
# 만약 max값이 두개이상일 때 이렇게 사용한다면
# max값 중 가장 빠른 idx가 사용됨!

if result.count(max(result)) >= 2 :
    print('?')
else:
    idx = result.index(max(result))
    print(word_list[idx])



# 그렇다면 2개이상일 때 그 인자를 출력(알파벳 순)하는 방법은?
# 간격없이 출력하기
'''new_list =[]
for i in range(result.count(max(result))):
    idx = result.index(max(result))
    #print(word_list[idx],end=' ')
    #word_list.pop(idx)
    new_list.append(word_list[idx])
    word_list.pop(idx)
new_list.sort()
for i in range(len(new_list)):
    print(new_list[i],end='')'''

