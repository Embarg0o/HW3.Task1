# Условие. Считается, что один год, прожитый собакой, эквивалентен семи человеческим годам.
# При этом зачастую не учитывается, что собаки становятся абсолютно взрослыми уже к двум годам.
# Таким образом, многие предпочитают каждый из первых двух лет жизни собаки приравнивать к 10,5 года
# человеческой жизни, а все последующие – к четырем. Напишите программу, которая будет переводить
# человеческий возраст в собачий с учетом указанной выше логики. Убедитесь, что программа корректно
# работает при пересчете возраста собаки меньше и больше двух лет. Также программа должна выводить
# сообщение об ошибке, если пользователь ввел отрицательное число, либо не числовое значение.
two_years = 10.5
later_year = 4
total_age = 0
puppy = 2

line = input('Введите возраст человека для перевода его в собачий возраст: ')
try:
    line = int(line)
except ValueError:
    print("Ошибка, введите возраст человека в числовом формате.")
else:
    if line >= 0:
        if line <= puppy:
            total_age = line * two_years
            print('Указаный человеческий возраст равен %.1f собачьим годам.' % total_age)
        else:
            total_age = line * later_year + 2 * (two_years - later_year)
            print('Указаный человеческий возраст равен %.1f собачьим годам.' % total_age)
    else:
        print('Ошибка, введите не отрицательное число.')