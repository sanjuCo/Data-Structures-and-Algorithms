def rotate(nums, k):
    n=len(nums)
    k %=n

    nums.reverse()

    nums[:k] = reversed(nums[:k])

    nums[k:] = reversed(nums[k:])