"""Игра угадай число. Версия 3.0
Компьютер сам загадывает и сам угадывает число менее, чем за 20 попыток
"""
import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число, при этом область поиска на каждом шаге цикла урезаем

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    maximum = 101
    minimum = 1

    while True:
        count += 1
        predict_number = np.random.randint(minimum, maximum)  # угадывание на каждом шаге происходит в урезанном диапозоне
        if number == predict_number:
            break                       # выход из цикла, если число угадано
        elif number > predict_number:   # если загаданное число больше,
            minimum = predict_number    # то присваиваю минимальному значению диапазона предложенное число
        elif number < predict_number:
            maximum = predict_number    # аналогично с максимальным значением
       
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    
    return score


if __name__ == "__main__":
    # RUN
    print(score_game(random_predict))
