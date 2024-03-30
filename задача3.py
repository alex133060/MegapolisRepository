a=open('rocket.csv',encoding='utf-8').readlines()
a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip().split(',')
    print(*a[i])
while True:
    date=input()
    if date=='sleep':
        break
    flag=0
    for x in a:
        if x[0]==date:
            """
            нахожу нужную дату, чтобы вывести все нужные данные
            """
            print(f'Шифр {x[1]} от {x[2]} был получен {x[0]}')
            flag=1
            break
    if flag==0:
        print('Ничего не найдено')