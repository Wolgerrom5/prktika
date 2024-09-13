import keyword
name = input('Введите имя: ')

if name in keyword.kwlist:
    print('Имя не подходит')
    exit()
if name[0].isdigit():
    print('Имя не подходит')
    exit()
for i in name:
    if ord('а') <= ord(i) <= ord('я') or ord('А') <= ord(i) <= ord('Я'):
        print('Имя не подходит')
        exit()
for i in name:
    if not (i.isalpha() or i.isdigit() or i == '_'):
        print('Имя не подходит')
        exit()
print('Имя подходит:)')