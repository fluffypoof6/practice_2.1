students = []

with open("students.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        name, grades_str = line.split(":")
        grades = [int(x) for x in grades_str.split(",")]
        
        avg = sum(grades) / len(grades)
        students.append((name, avg, grades))

with open("result.txt", "w", encoding="utf-8") as f:
    f.write("Студенты со средним баллом выше 4.0:\n")
    for name, avg, grades in students:
        if avg > 4.0:
            f.write(f"{name}: {avg:.2f} ({grades})\n")
            print(f"{name}: {avg:.2f}")
            
best = max(students, key=lambda x: x[1])
print(f"\nЛучший студент: {best[0]} со средним баллом {best[1]:.2f}")