ticket_number = 1
lucky = False
while not lucky:
    number = input(f"Введите номер билета: ")
    if len(number) % 2 == 0:
        middle = len(number) // 2
        first_sum = sum(int(i) for i in number[:middle])
        second_sum = sum(int(i) for i in number[middle:])
        if first_sum == second_sum:
            print(f" {ticket_number}")
            lucky = True
        else:
            print(f"Несчастливый билет")
    else:
        print(f"количество цифр нечетное")
    ticket_number += 1