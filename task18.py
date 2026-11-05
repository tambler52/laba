import time

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            line = "время: " + current_time + " | функция: " + func.__name__ + " | args: " + str(args) 
            + " | kwargs: " + str(kwargs)
            with open(filename, "a", encoding="utf-8") as file:
                file.write(line)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_calls("file.txt")
def summa(a, b):
    return a + b


print("результат:", summa(5, 3))
