import random

def get_string_random(length, sb = 0):
    number = '0123456789'
    low_alpha = 'abcdefghijklmnopqrstuvwxyz'
    up_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbol = '!@$%^&<>'
    if sb == 0:
        get_string = number + low_alpha + up_alpha
    else:
        get_string = number + low_alpha + up_alpha + symbol
    st = ''
    for i in range(0,length):
        st += random.choice(get_string)
    return st


print(get_string_random(10))