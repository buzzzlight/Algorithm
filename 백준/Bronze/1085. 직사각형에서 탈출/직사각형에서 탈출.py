x, y, w, h = map(int, input().split())

a = w - x
b = h - y

num = [a, b, x, y]

print(min(num))