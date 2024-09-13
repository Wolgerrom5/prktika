sts = input('Введите предложение: ').strip()
perevern = sts.split()[::-1]
perevern_1=' '.join(perevern)
print(perevern_1)