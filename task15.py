
prodazhi = [
    {"name": "Яблоко", "price": 50, "count": 10},
    {"name": "Груша", "price": 70, "count": 5},
    {"name": "Апельсин", "price": 80, "count": 3}
]
itog = {}  
for tovar in prodazhi:
    name = tovar["name"]
    viruchka = tovar["price"] * tovar["count"]
    itog[name] = viruchka
print("Выручка по товарам:")
for name in itog:
    print(name, "-", itog[name], "бун.")
max_summa = 0
top_tovar = ""
for name in itog:
    if itog[name] > max_summa:
        max_summa = itog[name]
        top_tovar = name
print("самый прибыльный товар:", top_tovar, "(выручка:", max_summa, "бун.)")
print("уникальных наименований:", len(itog))