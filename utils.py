import re

def remove_substring(string, substring, replacement):
    if substring in string:
        return string.replace(substring, replacement)
    return string

def remove_slash_n(string):
    return remove_substring(string, '\n', ' ')

def remove_td(string):
    temp =remove_substring(string, '<td>', ' ')
    return remove_substring(temp, '</td>', ' ')

def remove_tags(string):
    return re.sub(r'<.*?>', ' ', str(string))

def remove_br(string):
    return re.sub(r'<.*?>', ' ', str(string))

def remove_dash_and_space(string):
    return re.sub(r'-\ ', '', str(string))


def remove_dash(string):
    return remove_substring(string, '-', ' ')

def strip(string):
    return string.strip()