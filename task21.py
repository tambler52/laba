import time


def zamer_vremeni(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        time_ms = (end_time - start_time) * 1000
        
        print("функция выполнялась:", time_ms, "мс")
        
        return result
    return wrapper


@zamer_vremeni
def summa(a, b):
    return a + b

print("результат сложения:", summa(5, 3))
print()
