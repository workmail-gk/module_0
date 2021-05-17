import numpy as np  # Устанавливаем библиотеку "numpy" и даем условное название "np"

count = 0  # Счетчик попыток
number = np.random.randint(1, 101)  # Генирируем слуайное число
print("Загадано число от 1 до 100")  # Выводим на экран


def score_game(game_core):
    count_ls = []  # Создаем пустой список
    np.random.seed(1)  # Фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим
    random_array = np.random.randint(1, 101, size=1000)  # Создаем переменную и присваиваем ей сгенерированое число
    for number in random_array:
        count_ls.append(game_core(number))  # Добавляем в ранее созданный пустой список значение
    score = int(np.mean(count_ls))  # Вычисляем среднее арифметическое значение
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")  # Выводим на экран
    return score  # Возвращаем полученное значение


def game_core_v3(number):  # Улучшенная логическая функция
    count = 1
    minimum = 1  # Задаем минимальное значение
    maximum = 101  # Задаем максимальное значение
    predict = (minimum + maximum) // 2  # Дополниетельное условия для сокращения попыток

    while number != predict:
        count += 1
        if number > predict:
            minimum = predict
        else:
            maximum = predict
        predict = (minimum + maximum) // 2
    return count


score_game(game_core_v3)  # Запускаем функцию
