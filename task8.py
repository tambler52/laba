import random
chislo = random.randint(1, 100)
while True:
    guess = int(input("введите число: "))
    if guess > chislo:
        print("Меньше") 
    elif guess < chislo:
        print("Больше")
    else:
        print("угадали")
        break