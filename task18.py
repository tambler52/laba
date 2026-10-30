import time


def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            with open(filename, "a", encoding="utf-8") as file:
                file.write("Время: " + current_time + ", Функция: " + func.__name__ + ", args: " + str(args) + ", kwargs: " + str(kwargs) + "\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_calls("file.txt")
def summa(a, b):
    return a + b


print("Результат:", summa(5, 3))
print("Результат:", summa(10, 20))