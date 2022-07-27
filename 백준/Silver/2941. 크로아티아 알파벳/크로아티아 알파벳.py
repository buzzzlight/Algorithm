word = input()
croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia_alphabet:
    count = word.replace(i, '*')
    word = count # word가 초기화 되지 않도록

print(len(count))