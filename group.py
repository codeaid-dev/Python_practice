list = [1,2,3,'a','b','c',1,2,3,'a','b','c',1,2,3,'a','b','c']
groups = []
tmp = []

while True:
    if not list:
        break

    for i in range(1, len(list)):
        if list[0] == list[i]:
            tmp.append(list[i])
    tmp.append(list[0])

    rm = list[0]
    while True:
        if rm in list:
            list.remove(rm)
        else:
            break

    print(tmp)
    print('groups1: ' + str(groups))
    groups.append(tmp[:])
    print('groups2: ' + str(groups))
    print('list: ' + str(list))
    tmp.clear()

print(list)
print(groups)
