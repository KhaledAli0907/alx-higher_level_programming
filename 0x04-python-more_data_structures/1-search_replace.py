#!/usr/bin/python
def search_replace(my_list: list, search, replace):
    index = 0
    newList = my_list.copy()

    for i in range(len(my_list)):
        if search == my_list[i]:
            newList[i] = replace
    return newList
