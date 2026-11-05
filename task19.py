def cache(func):
    saved_results = {}

    def wrapper(*args,**kwargs):
        key = str(args) + str(kwargs)
        if key in saved_results:
            print("резулитат взят из кэша",args,kwargs)
            return saved_results[key]
        if key not in saved_results:
            print("считаем",args,kwargs)
            res = func(*args,**kwargs)
            saved_results[key] = res
            return res
        
    return wrapper

@cache
def summa(a,b):
    res = a + b
    return res
print(summa(2,4))
print(summa(2,4))



