def flatten_list(spisok):
    i = 0
    while i < len(spisok):
        
        if type(spisok[i]) == list:
            vlozh = spisok[i]
            flatten_list(vlozh)
            spisok.pop(i)
            j = 0
            while j < len(vlozh):
                spisok.insert(i + j, vlozh[j])
                j += 1
        else:
            i += 1
list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
print("до:", list_a)
flatten_list(list_a)
print("после:", list_a)