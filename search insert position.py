nums = [1, 3, 5, 6]

target = int(input("Enter the number to search/insert: "))

position = 0
for i in range(len(nums)):
    if nums[i] >= target:
        position = i
        break
else:
    position = len(nums)

print("The number should be at index:", position)