city = input('Введите список городов через пробел:').split()
first = 'Петя'
ska = city[0][-1].lower()
for i in range(1, len(city)):
    if city[i][0].lower() != ska:
        if first == 'Петя':
            print('Вася выиграл!)')
        else:
            print('Петя выиграл!)')
        break
    if city[i][-1].lower() in ['ы', 'ь', 'ё']:
        ska = city[i][-2].lower()
        if first == "Петя":
            first = "Вася"
        else:
            first = "Петя"
    else:
        ska = city[i][-1].lower()
        if first == "Петя":
            first = "Вася"
        else:
            first = "Петя"

else:
    print(f"Выиграл {first}")