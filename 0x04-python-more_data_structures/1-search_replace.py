#!/usr/bin/python3
def search_replace(my_list: list, search, replace):
    newList = my_list.copy()

    for i in range(len(my_list)):
        if search == my_list[i]:
            newList[i] = replace
    return newList
