A, B = input().split()

A = A.replace('6', '5')
B = B.replace('6', '5')
print(int(A) + int(B), end=' ')
A = A.replace('5', '6')
B = B.replace('5', '6')
print(int(A) + int(B))
