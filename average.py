# get a list of grades and find the average

# Steps:
#     ask for grades
#     add up all grades
#     divide by total numbers
#     tell the average
def get_grades():
    result = []
    grade = 'none yet'
    while True:
        grade = input('enter a grade(enter "done" to stop):')
        if grade == "done":
            break
        numeric_grade = float(grade)
        result.append(numeric_grade)
    return result


grades = get_grades()
number_of_grades = len(grades)
total = 0
average = ''
for grade in grades:
    total = total + grade
average = total // number_of_grades
print(average, 'was the average grade')
