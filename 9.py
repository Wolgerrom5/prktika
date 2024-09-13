sts= input('Введите предложение: ')
ska=sts.split()
povtor=[]
for i in range(len(ska)):
    for j in range(i+1,len(ska)):
        if ska[i]==ska[j]:
            povtor.append(ska[i])
print(''.join(povtor))