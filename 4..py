text = input()
count = 0
for i in set(text):
    count = text.count(i)
    if count == 3:
        print(i)