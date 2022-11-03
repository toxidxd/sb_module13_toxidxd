print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S.: Формулу смотреть на сайте


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда = 0.2836250150891709


def fact_num(number):
    factorial = 1
    for num in range(1, number + 1):
        factorial *= num
    return factorial


def degree_num(num, degree):
    count = 1
    for _ in range(1, degree + 1):
        count = count * num
    return count


precision = float(input("Введите точность: "))
x = int(input("Введите х: "))

result = 0
n = 0
addMember = 1


while abs(addMember) > precision:
    addMember = degree_num(-1, n) * (degree_num(x, (2 * n)) / fact_num((2 * n)))
    result += addMember
    n += 1
print("Сумма ряда =", result)
