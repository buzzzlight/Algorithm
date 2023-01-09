def solution(today, terms, privacies):
    ty, tm, td = map(int, today.split('.'))
    grade_dic = {}
    answer = []
    cnt = 1

    for term in terms:
        grade, month = term.split()
        grade_dic[grade] = int(month)

    for privacy in privacies:
        date, grade = privacy.split()
        y, m, d = map(int, date.split('.'))
        m += grade_dic[grade]
        while m > 12:
            y += 1
            m -= 12
        if y < ty:
            answer.append(cnt)
        elif y == ty:
            if m < tm:
                answer.append(cnt)
            elif m == tm:
                if d <= td:
                    answer.append(cnt)
        cnt += 1

    return answer