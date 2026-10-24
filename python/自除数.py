left = 1
right = 100
nums = []
for i in range(left, right + 1):
    idea = 1
    temp_num = i
    while temp_num != 0:
        temp_1 = temp_num % 10
        temp_num //= 10
        if temp_1 == 0 or i % temp_1 != 0:
            idea = 0
            break
    if idea == 1:
        nums.append(i)

print(nums)