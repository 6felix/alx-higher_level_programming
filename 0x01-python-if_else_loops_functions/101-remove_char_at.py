#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        newstr = str[0:n] + str[n+1:]
    else:
        newstr = str
    return newstr
