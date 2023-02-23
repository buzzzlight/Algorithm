gpa = []
grade = {
    "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0
}

for _ in range(20):
    gpa.append(input().split())

gpa_sum = 0
total = 0

for i in gpa:
    if i[2] != 'P':
        gpa_sum += float(i[1])
        total += float(i[1]) * grade[i[2]]
    
print(round(total / gpa_sum, 6))