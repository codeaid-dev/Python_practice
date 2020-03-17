def quicksort(lst):
    left = []
    right = []
    if len(lst) <= 1:
        return lst

    # データの状態に左右されないためにrandom.choice()を用いることもある。
    # pivot = random.choice(lst)
    pivot = lst[len(lst)-1]
    pivot_count = 0

    for ele in lst:
        if ele < pivot:
            left.append(ele)
        elif ele > pivot:
            right.append(ele)
        else:
            pivot_count += 1
    left = quicksort(left)
    right = quicksort(right)
    return left + [pivot] * pivot_count + right

lst = [8, 5, 3, 6, 1, 9, 2, 7, 10, 4]
result = quicksort(lst)
print(lst)
print(result)
