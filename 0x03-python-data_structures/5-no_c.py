def no_c(my_string: str):
    return my_string.translate({ord(i): None for i in "Cc"})
