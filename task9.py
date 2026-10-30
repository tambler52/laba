length = {"м": 1, "км": 1000, "см": 0.01}
mass = {"кг": 1, "г": 0.001, "т": 1000}
time = {"с": 1, "мин": 60, "ч": 3600}
volume = {"л": 1, "мл": 0.001}
speed = {"м/с": 1, "км/ч": 1/3.6}

categories = ["длина", "масса", "время", "объём", "скорость"]

while True:
    print("категории:", categories)
    category = input("тип измерения: ").strip().lower()

    if category == "выход":
        break

    if category not in categories:
        print("нет такой категории")
        continue

    if category == "длина":
        units = length
    elif category == "масса":
        units = mass
    elif category == "время":
        units = time
    elif category == "объём":
        units = volume
    else:
        units = speed

    print("единицы:", list(units))
    source = input("из: ").strip()
    target = input("в:  ").strip()

    value_str = input("значение: ").strip()

    if not value_str.replace(".", "", 1).isdigit():
        print("нужно число")
        continue

    value = float(value_str)
    result = value * units[source] / units[target]

    print(value, source, "=", result, target)