print('Задача 2. Функция максимума')

# Юра пишет различные полезные функции для Питона, 
# чтобы остальным программистам стало проще работать.

# Он захотел написать функцию, 
# которая будет находить максимум из перечисленных чисел.
# Функция для нахождения максимума из двух чисел у него уже есть.
 
# Юра задумался: может быть, её можно как-то использовать 
# для нахождения максимума уже от трёх чисел?
 
 
# Напишите программу, 
# которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.


def max_number(a, b):
    max_num = (a + b) / 2 + abs(a - b) / 2
    return max_num


firstNumber = int(input("Введите первое число: "))
secondNumber = int(input("Введите второе число: "))
thirdNumber = int(input("Введите третье число: "))


maxNumber = max_number(max_number(firstNumber, secondNumber), thirdNumber)
print(maxNumber)
