import string
import random
with open('rocket.csv.csv', encoding='utf-8') as f:
    a = [[y.strip() for y in x.split(',')] for x in f.readlines()]
title = a.pop(0)
def create_commands():
    """
    данная функция создаёт команды для ракеты
    """
    pw = []
    for _ in range(3):
        pw.append(string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase)-1)])
    for _ in range(3):
        pw.append(string.ascii_uppercase[random.randint(0, len(string.ascii_uppercase)-1)])
    for _ in range(2):
        pw.append(string.digits[random.randint(0, len(string.digits)-1)])
    random.shuffle(pw)
    return ''.join(pw)
create_commands()

for j in range(len(a)):
    item = a[j]
    name = item[j][0]+item[j][1]
    a[j].append(name)
    pw = create_commands()
    a[j].append(pw)
with open('rocket_commands.csv', 'w') as f:
    f.write(','.join(title))
    for item in a:
        f.write('\n')
        f.write(','.join(item))