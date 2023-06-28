def print_tuple(*args):
    my_tuple = tuple(args)
    if len(my_tuple) > 10:
        my_tuple = my_tuple[:10]
    print(my_tuple)

print_tuple(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12, 13)
