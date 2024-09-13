text = input('Введите текст: ')
maximum = 0
count = 0
for i in range(len(text)):
    if text[i] == ' ':
        count += 1
    else:
        maximum = max(maximum, count)
        count = 0
maximum=max(maximum,count)
print(maximum)