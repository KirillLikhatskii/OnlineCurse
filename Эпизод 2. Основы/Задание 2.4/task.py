def task_1(str):
    text = str
    alphavit = [chr(i) for i in range(97, 123)]
    answer = {letter: 0 for letter in alphavit if letter in text}
    for text_letter in text:
        for letter in alphavit:
            if text_letter == letter:
                answer[letter] += 1
    return answer


def task_2(list):
    list = set(list)
    return sum(list)


def task_3(cities):
    return ', '.join(cities) + '.'


def task_4(a, b):
    a = set(a)
    b = set(b)
    answer = [x for x in a & b]
    return answer
