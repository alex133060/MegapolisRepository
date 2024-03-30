a=open('rocket.csv',encoding='utf-8').readlines()
a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip().split(',')
    print(*a[i])
d={}
"""
Создаю словарь для счёта шифр по месяцам и вкачестве ключа беру номер месяца
"""
for i in range(len(a)):
    key=a[i][0][5:7]
    if key not in d:
        d[key]=1
    else:
        d[key]+=1
d=dict(sorted(d.items()))
for x in d:
    print(f'В {x} было получено {d[x]} шифров'+'\n')

