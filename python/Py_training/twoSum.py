
def Sums(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter the target: "))
print(Sums(nums, target))
