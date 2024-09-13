sts=input('Введите предложение: ')
ska=sts.split()
all=sorted(ska, key=len)
print(' '.join(all))
