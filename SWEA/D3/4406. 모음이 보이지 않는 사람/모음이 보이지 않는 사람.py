T = int(input())
vowel = ['a', 'e', 'i', 'o', 'u']

for i in range(1, T + 1):
    word = input()
    for j in vowel:
        word = word.replace(j, '')
    print(f'#{i} {word}')