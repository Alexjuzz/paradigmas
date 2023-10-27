from math import sqrt

def correlation(first, second):
    # Вычисляем среднее значение для каждого списка
    mean_first = sum(first) / len(first)
    mean_second = sum(second) / len(second)

    # Вычисляем числитель формулы корреляции
    numerator = sum((x - mean_first) * (y - mean_second) for x, y in zip(first, second))

    # Вычисляем знаменатель формулы корреляции
    denominator = sqrt(sum((x - mean_first)**2 for x in first) * sum((y - mean_second)**2 for y in second))

    # Вычисляем корреляцию
    correlation = numerator / denominator if denominator != 0 else 0

    return correlation

if __name__ == '__main__':
    first = [1, 2, 3, 5]
    second = [2, 3, 4, 5]
    print(correlation(first, second))



