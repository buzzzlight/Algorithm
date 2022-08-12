word = input()
ban = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

for i in word:
    if i in ban:
        word = word.replace(i, '')
print(word)