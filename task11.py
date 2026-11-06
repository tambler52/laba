age = int(input("введите возраст"))
zp = int(input("введите зп"))
kredit = int(input("введите размер кредита"))
srok = int(input("введите срок"))
kreditistory = input("какая у вас кредитная история")
poruchitely = input("есть поручители")
zalog = input("есть залог")
minzp = 858
platezh = kredit/srok
sootnoshenie = platezh/zp *100
print("ежемесячный платеж:",platezh, "руб.")
print("соотношение:",sootnoshenie, "% от дохода")
if zp < minzp:
    print("кредит не одобрен")
    exit()

if sootnoshenie > 50:
     print("Категория риска: КРИТИЧЕСКИЙ")
     print("Кредит ОТКЛОНЕН")
elif sootnoshenie > 30:
    
    if zalog == "да" or poruchitely == "да":
        print("Категория риска: ВЫСОКИЙ")
        print("Предлагаемая ставка: 20% годовых")
        print("Кредит одобрен")
    else:
        print("Категория риска: КРИТИЧЕСКИЙ")
        print("Кредит ОТКЛОНЕН")
else:
    if kreditistory == "плохая":
        print("Категория риска: ВЫСОКИЙ")
        print("Кредит ОТКЛОНЕН")
    elif kreditistory == "удовлетворительная":
        print("Категория риска: СРЕДНИЙ")
        print("Предлагаемая ставка: 18% годовых")
        print("Кредит ОДОБРЕН")
    else:
        
        if age < 21 or age > 65:
            print("Категория риска: СРЕДНИЙ")
            print("Предлагаемая ставка: 15% годовых")
            print("Кредит ОДОБРЕН")
        else:
            print("Категория риска: НИЗКИЙ")
            print("Предлагаемая ставка: 12% годовых")
            print("Кредит ОДОБРЕН")









