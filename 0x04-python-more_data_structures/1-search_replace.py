#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_Slist = []
    for i in my_list:
        if i == search:
            my_Slist.append(replace)
        else:
            my_Slist.append(i)
    return my_Slist
