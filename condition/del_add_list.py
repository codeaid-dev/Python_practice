list = [1,2,3,4,5,6,7,8,9,10]
while True:
    if not list:
        break
    del list[0]
    print(list)

for i in range(1, 11):
    list.append(i)
    print(list)
