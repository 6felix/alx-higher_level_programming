#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for keys in a_dictionary:
        if keys is key:
            a_dictionary[keys] = value
            return a_dictionary
    a_dictionary[key] = value
#   a_dictionary.update({key:value})
    return a_dictionary
