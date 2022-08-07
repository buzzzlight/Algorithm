T = int(input())
thirty = ['09', '11', '04', '06']
thirty_one = ['01', '03', '05', '07', '08', '10', '12']

for i in range(1, T + 1):
    date = input()
    if 1 <= int(date[4:6]) <= 12:
        if int(date[4:6]) == 2:
            if int(date[6:8]) < 29:
                print(f'#{i} {date[0:4]}/{date[4:6]}/{date[6:8]}')
            else:
                print(f'#{i} -1')
        if date[4:6] in thirty:
            if int(date[6:8]) < 31:
                print(f'#{i} {date[0:4]}/{date[4:6]}/{date[6:8]}')
            else:
                print(f'#{i} -1')
        if date[4:6] in thirty_one:
            if int(date[6:8]) < 32:
                print(f'#{i} {date[0:4]}/{date[4:6]}/{date[6:8]}')
            else:
                print(f'#{i} -1')
    else:
        print(f'#{i} -1')