lst = [132, 434, 432, '343', '454']

def func(x):
    #return lst, int(lst) if isinstance(lst, str) else str(lst)
    if isinstance(x, int):
        x = str(x)
    else:
        x = int(x)
    
    
    return x
        
b = list(map(func, lst))
print(b)




    

