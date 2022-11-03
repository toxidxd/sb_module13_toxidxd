print('Задача 6. Маятник ')

# Известно, что амплитуда качающегося маятника с каждым разом затухает
# на 8,4% от амплитуды прошлого колебания. 
# Если качнуть маятник,
# то, строго говоря, он не остановится никогда, 
# просто амплитуда будет постоянно уменьшаться до тех пор, 
# пока мы не сочтём такой маятник остановившимся. 
 
# Напишите программу, 
# определяющую, сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится. 
 
# Программа получает на вход
# начальную амплитуду колебания в сантиметрах 
# и конечную амплитуду его колебаний,
# которая считается остановкой маятника. 

# Обеспечьте контроль ввода.

# Пример:

# Введите начальную амплитуду: 1
# Введите амплитуду остановки: 0.1
 
# Маятник считается остановившимся через 27 колебаний


def fluctuations_count(amp, stop_amp):
    count = 0
    while amp >= stop_amp:
        amp = amp - (amp * 0.084)
        count += 1

    return count


amplitude = float(input("Введите начальную амплитуду: "))
stopAmp = float(input("Введите амплитуду остановки: "))

fluctCount = fluctuations_count(amplitude, stopAmp)

print(f"Маятник считается остановившимся через {fluctCount} колебаний.")
