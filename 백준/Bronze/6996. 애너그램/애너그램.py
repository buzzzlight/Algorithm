T = int(input())

for i in range(T):
    A, B = input().split()
    list_A = list(A)
    list_B = list(B)
    if len(A) == len(B):
        for j in list_A:
            if j in list_B:
                list_B.remove(j)
                if len(list_B) == 0:
                    print(A, '&', B, 'are anagrams.')
            else:
                print(A, '&', B, 'are NOT anagrams.')
    else:
        print(A, '&', B, 'are NOT anagrams.')