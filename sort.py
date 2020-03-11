nums = [30, 50, 10, 40, 20]
# バブルソート
'''
loop = True
while loop:
    loop = False
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            loop = True
'''
# バブルソート
for i in range(len(nums)):
    for j in range(1, len(nums)):
        if (nums[j-1] > nums[j]):
            nums[j], nums[j-1] = nums[j-1], nums[j]

print(nums)

# 挿入ソート（インサーションソート）
lst = [300, 500, 100, 400, 200]
for i in range(1, len(lst)):
        j = i - 1
        ele = lst[i]
        while lst[j] > ele and j >= 0:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = ele

print(lst)