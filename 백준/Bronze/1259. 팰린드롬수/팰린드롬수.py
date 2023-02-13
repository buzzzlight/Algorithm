while True:
    num = input()
    if num == '0':
        break
    elif list(num) == list(reversed(list(num))):
        print('yes')
    else:
        print('no')