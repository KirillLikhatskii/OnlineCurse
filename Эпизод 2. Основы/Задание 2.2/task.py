# Пример 1
def task_1(A):
    answer = 0
    for i in range(0, len(A)):
        if A[i] > 0:
            answer = answer + A[i]
    return answer


# Пример 2
def task_2(A):
    return sum(A)/len(A)


# Пример 3
def task_3(A):
    srznach = sum(A) / len(A)
    sqdev = []
    for i in range(0, len(A)):
        sqdev.append((A[i] - srznach) ** 2)
    return (sum(sqdev) / len(sqdev)) ** 0.5
