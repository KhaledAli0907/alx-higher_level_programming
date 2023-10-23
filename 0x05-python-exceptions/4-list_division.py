#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length) -> list:
    result = 0
    l = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            result = 0
            print("wrong type")
            continue
        except ZeroDivisionError:
            result = 0
            print("division by 0")
            continue
        except IndexError:
            result = 0
            print("out of range")
            continue
        finally:
            l.append(result)

    return l
