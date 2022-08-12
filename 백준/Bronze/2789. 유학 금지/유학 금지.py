word = input()
ban = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

for i in word:
    if i in ban:
        word = word.replace(i, '')
print(word)

# 이게 더 좋을듯 ...
word = input()                        
remove_word = list('CAMBRIDGE')       
new_word = ''                         # 새로운 문자열 받을 곳 만듬
for i in word:                        
    if not i in remove_word:          # 겹치는 것이 없는 i를
        new_word += i                 # new_word에 추가시킴

print(new_word)
