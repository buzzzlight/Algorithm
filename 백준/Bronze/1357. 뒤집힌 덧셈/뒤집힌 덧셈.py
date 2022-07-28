X, Y = map(int,input().split())

def Rev(X):
    X = str(X)
    return int(X[::-1])

print(Rev(Rev(X) + Rev(Y)))