def solution(t, p):
    t_list = []
    answer = 0

    for i in range(len(t)-(len(p)-1)):
        t_list.append(t[i:i+len(p)])

    for t in t_list:
        if int(t) <= int(p):
            answer += 1

    return answer