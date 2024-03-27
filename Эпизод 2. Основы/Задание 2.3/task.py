
def task_1(str):
    answer = str.split()
    return len(answer[-1])


def task_2(str):
    text1 = str.split()
    answer = []
    save = ''
    for i in range(0, len(text1)):
        if i % 2 == 0:
            save = text1[i]
        else:
            answer.append(text1[i])
            answer.append(save)
    if len(text1) % 2 != 0:
        answer.append(save)
    return ' '.join(answer)


def task_3(str):
    words = str.split()
    save = ''
    answer = 0
    for word in words:
        if word[0] == save:
            answer += 1
        save = word[-1]
    return answer
