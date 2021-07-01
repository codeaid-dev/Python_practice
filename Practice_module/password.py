import string
import random

'''
wd = [string.printable[index] for index in [random.randint(0, len(string.printable) - 1) for num in range(16)]]
map_wd = map(str, wd)
result = ''.join(map_wd)
print(result)
'''
password = []
ex = [' ', '\t', '\r', '\x0b', '\x0c']
for num in range(16):
    index = random.randint(0, len(string.printable) - 1)
    wd = string.printable[index]
    if wd in ex:
        password.append('@')
    else:
        password.append(wd)

result = ''.join(password)
print(result)
