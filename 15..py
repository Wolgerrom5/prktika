number = input('Введите число: ')
print("\n" * 25)
for i in range(10):
    attempt = input('Введите ваше предположение: ')
    bulls = 0
    cows = 0
    for j in range(4):
        if attempt[j] == number[j]:
            bulls += 1
        elif attempt[j] in number:
            cows += 1
    print(f'Быков: {bulls}, Коров: {cows}')
    if bulls == 4:
        print('Победа')
        break
else:
    print('Проигрыш!')