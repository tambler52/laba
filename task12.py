tekst = input("введите текст: ")
slova = tekst.lower().split()  
colvo = len(slova)
print("Общее количество слов:", colvo)


print("частота слов:")
chastota = []  
for word in slova:
    if word not in chastota:
        count = slova.count(word)
        print(word, "-", count, "раз")
        chastota.append(word)  


max_count = 0
pop = ""
for word in slova:
    count = slova.count(word)  
    if count > max_count:
        max_count = count
        pop = word
print("самое частое слово:", pop, "(встречается", max_count, "раз)")


shortest = slova[0]
longest = slova[0]

for word in slova:
    if len(word) < len(shortest):
        shortest = word
    if len(word) > len(longest):
        longest = word

print("Самое короткое слово:", shortest)
print("Самое длинное слово:", longest)


filtered = []
for word in slova:
    if len(word) >= 3:
        filtered.append(word)

print(" после фильтрации:", len(filtered))

max_count2 = 0
pop2 = ""
for word in filtered:
    count = filtered.count(word)
    if count > max_count2:
        max_count2 = count
        pop2 = word

if pop2 != "":
    print("Самое частое слово после фильтрации:", pop2, "(встречается", max_count2, "раз)")