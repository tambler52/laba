minut = int(input("введите минуты"))
sms = int(input("введите смс"))
internet = int(input("введите интернет"))
basicprice = 24.99
print("базовая цена:",round(basicprice, 2))
exminprice = 0
exsmsprice = 0
exintprice = 0
if minut > 60:
    extraminut = minut - 60
    print("доп минуты" , extraminut)
    exminprice = extraminut*0.89
    print("цена за доп минуты", round(exminprice, 2))

if sms > 30:
    extrasms = sms - 30
    print("доп смс" , extrasms)
    exsmsprice = extrasms*0.59
    print("цена за доп смс" , round(exsmsprice, 2))

if internet > 1024:
    extrainternet = internet - 1024
    print("доп интернет" , extrainternet)
    exintprice = extrainternet*0.79
    print("цена за доп интернет" , round(exintprice, 2))


extraprice = exminprice + exsmsprice + exintprice
print("доп цена",round(extraprice, 2))
sum = (basicprice + extraprice) + (basicprice + extraprice)*0.02
print("доп цена с налогом",round(sum, 2))



            
    

