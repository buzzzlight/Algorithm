taebo = input()
taebo = taebo.split('0')
cnt_left = taebo[0].count('@')
cnt_right = taebo[1].count('@')
print(cnt_left, cnt_right)