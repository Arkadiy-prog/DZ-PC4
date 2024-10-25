KOD
#Домашняя работа по уроку "Цикл for. Элементы списка.
# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустые списки для простых и не простых чисел
primes = []
not_primes = []

# Перебираем каждый элемент списка numbers
for num in numbers:
    # Пропускаем число 1, так как оно не является ни простым, ни составным
    if num == 1:
        continue

    # Предполагаем, что число простое
    is_prime = True

    # Проверяем делимость числа
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # Добавляем число в соответствующий список
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим результаты
print("Простые числа:", primes)
print("Не простые числа:", not_primes)


PC
Простые числа: [2, 3, 5, 7, 11, 13]
Не простые числа: [4, 6, 8, 9, 10, 12, 14, 15]

Process finished with exit code 0
