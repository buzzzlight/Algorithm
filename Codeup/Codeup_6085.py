w, h, b = map(int, input().split())
p = round(w * h * b / 8 / 1024 / 1024, 2)
print(p, 'MB')