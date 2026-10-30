dohody = {}
rashody = {}

while True:
    print("1. доход , 2. расход , 3. итог , 4. выход")
    vybor = input("действие:").strip()

    if vybor == "4":
        break

    elif vybor == "1":
        kat = input("категория дохода:").strip().lower()
        summa = float(input("сумма:").strip())
        
        if kat in dohody:
            dohody[kat] = dohody[kat] + summa
        else:
            dohody[kat] = summa

    elif vybor == "2":
        kat = input("категория расхода:").strip().lower()
        summa = float(input("сумма:").strip())
        
        if kat in rashody:
            rashody[kat] = rashody[kat] + summa
        else:
            rashody[kat] = summa

    elif vybor == "3":
        print("твои финансы")
        
        vsego_dohod = 0
        for kat in dohody:
            print("доход", kat, ":", dohody[kat])
            vsego_dohod = vsego_dohod + dohody[kat]
            
        vsego_rashod = 0
        for kat in rashody:
            print("расход", kat, ":", rashody[kat])
            vsego_rashod = vsego_rashod + rashody[kat]
            
        print("всего доходов:", vsego_dohod)
        print("всего расходов:", vsego_rashod)
        
        ostatok = vsego_dohod - vsego_rashod
        print("остаток:", ostatok)
        
        print("совет")
        if ostatok > 0:
            print("отлично, ты в плюсе! отложи эти деньги на крупную покупку.")
        elif ostatok == 0:
            print("ты потратил всё. попробуй в следующем месяце отложить хоть что-то.")
        else:
            print("ты в минусе! срочно сократи расходы на развлечения и другое.")