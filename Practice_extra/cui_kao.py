result = ''
for row in range(6):
    for col in range(15):
        if row in (0,6) and col in (2,12):
            result += '*'
        elif row == 1 and col in (1,13):
            result += '*'
        elif row == 2 and col in (0,3,4,5,9,10,11,14):
            result += '*'
        elif row == 3 and col in (0,14):
            result += '*'
        elif row == 4 and col in (1,5,6,7,8,9,13):
            result += '*'
        elif row == 5 and col in (2,12):
            result += '*'
        else:
            result += ' '
    result += '\n'
print(result)