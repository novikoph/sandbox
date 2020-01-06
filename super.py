import random

home = input('Кто играет дома?: ')
visitor = input('Кто играет в гостях?: ')
result = []

for i in range(100):
    preres = random.randint(0, 2)
    result.append(preres)

print(result)

homeWin     = result.count(1)
visitorWin  = result.count(2)
draw        = result.count(0)

total = [homeWin, visitorWin, draw]
print(total)

max = max(total)
print(max)

if homeWin == max:
    print('Победит команда ' + home)
elif visitorWin == max:
    print('Победит команда ' + visitor)
else:
    print('Ничья')

