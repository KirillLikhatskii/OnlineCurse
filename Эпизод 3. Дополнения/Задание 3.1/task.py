def task_1(text):
    sentences = text.split('. ')
    last_point = sentences[-1].split('.')
    sentences[-1] = last_point[0]
    answer = {sentence: 'none' for sentence in sentences}
    for sentence in sentences:
        words = sentence.split()
        answer[sentence] = len(words)
    return answer

def task_2(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5