def check(text):
    spisok = []
    for i in text:
        if i in '([{<':
            spisok.append(i)
        elif i in ')]}>':
            if spisok and open(spisok.pop(), i):
                continue
            else:
                return 'Скобки расставлены неправильно'
    if spisok:
        return 'Скобки расставлены неправильно'
    return 'Скобки расставлены правильно'


def open(open, close):
    return (open == '(' and close == ')') or \
        (open == '[' and close == ']') or \
        (open == '{' and close == '}') or \
        (open == '<' and close == '>')


text = input('Введите текст со скобками: ')
result = check(text)
print(result)
