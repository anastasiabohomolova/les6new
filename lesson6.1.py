lst_r = [123, 344, 434, '343', '4']

lst_n = list(map(lambda a: int(a) if isinstance(a, str) else str(a), lst_r))  

print(lst_n)


