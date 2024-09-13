hint = input('Введите подсказку: ')
word = input('Введите слово:')
print("\n" * 25)
wrd = ["*" for _ in range(len(word))]
for i in range(10):
    print(f'{hint}')
    print(" ".join(wrd))
    question = input('Буква или слово? (0 - буква, 1 - слово): ')
    if question == "0":
        letter = input('')
        if len(letter) != 1 or not letter.isalpha():
            print('Введите ещё раз: ')
            continue
        for j in range(len(word)):
            if word[j] == letter:
                wrd[j] = letter
    elif question == "1":
        guess = input("Введите слово: ")
        if guess == word:
            print("Победа!")
            break
        else:
            print("Неверно.")
    else:
        print("Попробуйте снова.")
if i == 9:
    print('Проигрыш!')
