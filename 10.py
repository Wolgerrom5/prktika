sts = input('Введите предложение: ').strip()
ska = sts.split()
usl = []
first = ska[0]
for i in ska:
    if i != first and len(i) == len(set(i)):
       usl.append(i)
       print(i, end=',')