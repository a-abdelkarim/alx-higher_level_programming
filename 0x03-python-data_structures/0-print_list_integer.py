def print_list_integer(my_list=[]):
    for elem in my_list:
        if type(elem) == int:
             print("{:d}".format(elem))
