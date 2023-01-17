while True:
    inp = input()
    stack = []
    flag = False

    if inp == '.':
        break

    for i in inp:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = True
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = True
                break
    
    if flag == False and not stack:
        print('yes')
    else:
        print('no')