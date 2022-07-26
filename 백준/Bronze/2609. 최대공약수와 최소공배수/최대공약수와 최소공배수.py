A, B = map(int,input().split())

def gcd(A, B): # 최대공약수
    for i in range(min(A, B), 0, -1):
        if A % i == 0 and B % i == 0:
            break
    return i

def lcm(A, B): # 최소공배수
    common_multiple = (A * B) / gcd(A, B)
    return common_multiple

print(gcd(A, B), int(lcm(A, B)), sep='\n')