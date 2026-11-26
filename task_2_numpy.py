import numpy as np

np.random.seed(1)

students = ["кивель", "мирчук", "ясюк", "бардышев", "мурков",
            "аксенов", "марко", "маляревич", "сахащик", "страх",
            "барановский", "станчик", "мацкевич", "комалов", "банчук",
            "радикевич", "ковальчук", "шевчук", "бойко", "мельник"]
subjects = ["матанализ", "оптика", "питон", "английский"]

grades = np.random.randint(3, 11, size=(len(students), len(subjects)))
print(grades)

student_avg = grades.mean(axis=1)
for i in range(len(students)):
    print(students[i], round(student_avg[i], 2))

best = np.argmax(student_avg)
worst = np.argmin(student_avg)
print("лучший студент:", students[best], student_avg[best])
print("худший студент:", students[worst], student_avg[worst])

subject_avg = grades.mean(axis=0)
for i in range(len(subjects)):
    print(subjects[i], round(subject_avg[i], 2))

print("самый простой предмет:", subjects[np.argmax(subject_avg)])
print("самый сложный предмет:", subjects[np.argmin(subject_avg)])

scholarship = []
for avg in student_avg:
    if avg >= 9:
        scholarship.append(350)
    elif avg >= 8:
        scholarship.append(320)
    elif avg >= 6:
        scholarship.append(280)
    elif avg >= 4:
        scholarship.append(200)
    else:
        scholarship.append(0)

for i in range(len(students)):
    print(students[i], round(student_avg[i], 2), scholarship[i])

print("общий фонд:", sum(scholarship))