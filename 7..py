sts = input('Введите текст: ').strip()
ska = sts.split()
shorts = min([len(i) for i in ska])
print(shorts)