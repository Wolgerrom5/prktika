text = input('Введите текст: ')
maximum = 0
count = 1
for i in range(1,len(text)):
    if text[i]==text[i-1]:
        count+=1
    else:
        maximum=max(maximum,count)
        count=1
maximum=max(maximum,count)
print(maximum)