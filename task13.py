stroka = (input("введите числа через пробел"))
slova = stroka.split()
chisla = []
for s in slova:
    chisla.append(float(s))
print("все числа:", chisla)
unikalnye = []
for num in chisla:
    if chisla.count(num) == 1:
        unikalnye.append(num)
print("уникальные числа:", unikalnye)
povtory = []
for num in chisla:
    if chisla.count(num) > 1 and num not in povtory:
        povtory.append(num)
print("повторки:", povtory)
chetnye = []
nechetnye = []
for num in chisla:
    
    if num == int(num): 
        if int(num) % 2 == 0:
            chetnye.append(num)
        else:
            nechetnye.append(num)
print("четные:", chetnye)
print("нечетные:", nechetnye)
otricatelnye = []
for num in chisla:
    if num < 0:
        otricatelnye.append(num)
print("отрицательные :", otricatelnye)
drobi = []
for num in chisla:
    if num != int(num):  
        drobi.append(num)
print(" дроби:", drobi)
summa = 0
for num in chisla:
    if num == int(num) and int(num) % 5 == 0:
        summa = summa + num
print("сумма чисел, кратных 5:", summa)
if len(chisla) > 0:
    print("самое большое:", max(chisla))
    print("самое маленькое:", min(chisla))
else:
    print("Список пуст.")

