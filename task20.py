def unique_elements(list_a):
    result = []
    for item in list_a:
        if type(item) == list:
            for x in unique_elements(item):
                if x not in result:
                    result.append(x)
        else:
            if item not in result:
                result.append(item)
    return result


list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print("исходный список:", list_a)
print("уникальные элементы:", unique_elements(list_a))