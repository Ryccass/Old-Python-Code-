def front_back(str):
    list_str = list(str)
    first_char = str[0]
    last_char = str[len(str) - 1]
    str_length = len(str)

    list_str[0] = ""
    list_str[len(list_str)-1] = ""
    list_str.insert(0, last_char)
    list_str.insert(str_length-1, first_char)
    normal_str = ''.join(list_str)
    print(normal_str)
    
front_back("kitten")