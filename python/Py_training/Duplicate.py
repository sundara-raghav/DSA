def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:  
                return True
    return False
num = list(map(int, input("Enter numbers: ").split()))
print(containsDuplicate(num))