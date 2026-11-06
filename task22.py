def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(len(args)):
                if type(args[i]) != expected_types[i]:
                    raise TypeError("неверный тип аргумента " + str(i + 1))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@type_check(int, int)
def add(a, b):
    return a + b


print("результат сложения:", add(2, 3))

print("проверка ошибки:")
print(add(2, "3"))