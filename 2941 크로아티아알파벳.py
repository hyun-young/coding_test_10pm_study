word = input()

croatia = ['dz=','c=','c-','d-','lj','nj','s=','z=']
# 틀렸던 이유
# 'dz=','z='가 있는데 'dz='형태를 먼저 검사해줘야됨
# 우선순위가 'dz='임


for crobet in croatia:
    # 문자열.replace('a','b') #문자열 내 a를 b로 바꾸기
    # replace는 다시 저장해야함
    word = word.replace(crobet,'*')
print(word)
print(len(word))