# Count Pairs Whose Sum is Less than Target


def countPairs(nums, target: int):
    c=0
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] < target:
                c += 1
    return c

nums = [-6,2,5,-2,-7,-1,3]
target = -2
print(countPairs(nums, target))


