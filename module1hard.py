print('Дополнительное практическое задание по модулю: "Базовые структуры данных". Задание "Средний балл":')
grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
print(grades)
students={'Johnny','Bilbo','Steve','Khendrik','Aaron'}
list_of_students=(sorted(students))
print(list_of_students)
list_of_average_grades=[(sum(grades[0])/len(grades[0])),(sum(grades[1])/len(grades[1])),(sum(grades[2])/len(grades[2])),
                     (sum(grades[3])/len(grades[3])),(sum(grades[4])/len(grades[4]))]
average_student_grades=dict(zip(list_of_students, list_of_average_grades))
print(average_student_grades)