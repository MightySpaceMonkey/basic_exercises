# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names = dict()

for student in students:
    if student['first_name'] not in names:
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1

for name, count in names.items():
    print(f'{name}: {count}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???
names = dict()

for student in students:
    if student['first_name'] not in names:
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1

max_count = 0
max_name = ''
for name, count in names.items():
    if count > max_count:
        max_count = count
        max_name = name

print(f'Cамое частое имя среди участников: {max_name}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???
classes_qty = 0
for students in school_students:

    names = dict()
    
    for student in students:
        if student['first_name'] not in names:
            names[student['first_name']] = 1
        else:
            names[student['first_name']] += 1

    max_count = 0
    max_name = ''
    for name, count in names.items():
        if count > max_count:
            max_count = count
            max_name = name

    classes_qty += 1

    print(f'Cамое частое имя в классе {classes_qty}: {max_name}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???
for study_class in school:
    male_qty = 0
    female_qty = 0
    for student in study_class['students']:
        if is_male[student['first_name']]:
            male_qty += 1
        else:
            female_qty += 1

    print(f"Класс {study_class['class']}: девочки {female_qty}, мальчики {male_qty}")



# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
male_qty = 0
female_qty = 0

for study_class in school:
    for student in study_class['students']:
        if is_male[student['first_name']]:
            male_qty += 1
        else:
            female_qty += 1

    if male_qty > female_qty:
        print(f'Больше всего мальчиков в классе {study_class["class"]}')
    else:
        print(f'Больше всего девочек в классе {study_class["class"]}')
