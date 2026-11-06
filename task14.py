stroka1 = input("")
stroka2 = input("")
chisla1 = stroka1.split()
chisla2 = stroka2.split()

spisok1 = []
for s in chisla1:
    spisok1.append(s)

spisok2 = []
for s in chisla2:
    spisok2.append(s)
print("первый набор:", spisok1)
print("второй набор:", spisok2)

obshie = []
for num in spisok1:
    if num in spisok2 and num not in obshie:
        obshie.append(num)
print("общие числа:", obshie)

tolko_v_pervom = []
for num in spisok1:
    if num not in spisok2 and num not in tolko_v_pervom:
        tolko_v_pervom.append(num)

tolko_vo_vtorom = []
for num in spisok2:
    if num not in spisok1 and num not in tolko_vo_vtorom:
        tolko_vo_vtorom.append(num)
print("есть только в первом наборе:", tolko_v_pervom)
print("есть только во втором наборе:", tolko_vo_vtorom)

vse_krome_obshih = []
for num in spisok1:
    if num not in obshie and num not in vse_krome_obshih:
        vse_krome_obshih.append(num)
for num in spisok2:
    if num not in obshie and num not in vse_krome_obshih:
        vse_krome_obshih.append(num)

print("все числа, кроме общих:", vse_krome_obshih)