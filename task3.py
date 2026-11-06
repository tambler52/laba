suma = int(input("Введите сумму"))
count100 = suma // 100
count50 = (suma - count100 * 100) // 50
count10 = (suma - count100*100 - count50 * 50) // 10
count5 = (suma - count100*100 - count50 * 50 - count10*10) // 5
count2 = (suma - count100*100 - count50 * 50 - count10*10 - count5*5) // 2
count1 = suma - count100*100 - count50 * 50 - count10*10 - count5*5 - count2*2
print("100:", count100, ";","50:" , count50 ,";", "10:" , count10 ,";", "5:" , count5 ,";", "2:" , count2 ,";", "1:" ,";", count1 )