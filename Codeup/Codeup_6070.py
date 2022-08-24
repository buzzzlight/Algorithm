n = int(input())

if n == 12 or n < 3:
    print('winter')
elif 2 < n < 6:
    print('spring')
elif 5 < n < 9:
    print('summer')
else:
    print('fall')