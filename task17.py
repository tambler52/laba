def merge_dicts(dict_a, dict_b):
    for key in dict_b:
        if key in dict_a:
            
            if type(dict_a[key]) == dict and type(dict_b[key]) == dict:
                merge_dicts(dict_a[key], dict_b[key])
            else:
                
                dict_a[key] = dict_b[key]
        else:
            
            dict_a[key] = dict_b[key]

dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}

print("Первый словарь:", dict_a)
print("Второй словарь:", dict_b)