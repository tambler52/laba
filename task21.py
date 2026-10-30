import time


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        time_ms = (end_time - start_time) * 1000
        
        print("функция", func.__name__, "выполнялась:", time_ms, "мс")
        
        return result
    return wrapper


@timing
def summa(a, b):
    return a + b


@timing
def wait_and_print():
    time.sleep(0.5)
    print("работа внутри функции завершена")


print("результат сложения:", summa(5, 3))
print()
wait_and_print()