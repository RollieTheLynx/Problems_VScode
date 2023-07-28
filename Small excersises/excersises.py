def twoSum(nums, target: int):
    for n in nums:
        for m in nums:
            if n + m == target:
                return nums.index(n), nums.index(m)


nums = [2,7,11,15]
target = 9
n, m = twoSum(nums, target)
print (n , m)

nums = [3,2,4]
target = 6
n, m = twoSum(nums, target)
print (n , m)

nums = [3,3]
target = 6
n, m = twoSum(nums, target)
print (n , m)