mas = list(map(int, input("Введите список: ").split())) # Запрашиваем список
print([i**2 for i in range(1, len(mas) + 1)]) # Генерирую список чисел в квадрате
