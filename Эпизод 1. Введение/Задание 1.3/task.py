# Пример 1
def task_1(n):
    answer = 0
    i = 1
    while i <= 10:
        answer = answer + 1 / i
        i = i + 1
    return answer


# Пример 2
def task_2(x, n):
    answer = 0
    i = 1
    while i <= 17:
        answer = answer + x / i
        i = i + 2
    return answer


# Пример 3
def task_3(n):
    answer = 1
    i = 1
    while i <= n:
        answer = answer * i
        i = i + 1
    return answer


# Пример 4
def task_4(x, n):
    answer = 1
    i = 2
    while i <= 9:
        answer = answer * ((x + i) / i)
        i = i + 1
    return answer


# Пример 5
def task_5(x, n):
    answer = 1
    i = 1
    while i <= 9:
        answer = answer + ((x*i) / (2*i))
        i = i + 1
    return answer - 4 # Не понял сути задания последовательность Y = 1 + xi/2i


# Пример 6
def task_6(n):
    answer = 1
    i = 2
    while i <= 20:
        answer = answer * i
        i = i + 2
    return answer
