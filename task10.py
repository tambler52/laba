cost = int(input("введите цену"))
age = int(input("введите возраст"))
dr = input("др?")
vip = input("vip?")
sale = 0
if cost > 1000:
    sale  = sale+10
    print("скидка 10%")
if age > 63:
    sale = sale + 5
    print("скидка 5%")
if dr == "да":
     sale = sale + 5
     print("скидка 5%")
if vip == "да":
    
    print("клиент вип")
    if sale < 15:
        sale = 15
    else:
        sale = sale
if sale > 25:
    sale = 25
    print("максимум 25%.")
final_price = cost - (cost * sale / 100)
print("скидка:", sale, "%")
print("сумма к оплате:",final_price ,"руб.")
