print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# полученное из исходного, записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123
 
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225


def flip_over(number):
    result = 0

    while number > 0:
        digit = number % 10
        result = result * 10 + digit
        number //= 10
    return result


firstNumber = int(input("Введите первое число: "))
secondNumber = int(input("Введите второе число: "))

firstNumber_flip = flip_over(firstNumber)
secondNumber_flip = flip_over(secondNumber)

print(f"Первое число наоборот {firstNumber_flip}")
print(f"Второе число наоборот {secondNumber_flip}\n")

print(f"Сумма: {firstNumber + secondNumber}")
print(f"Сумма наоборот: {firstNumber_flip + secondNumber_flip}")
