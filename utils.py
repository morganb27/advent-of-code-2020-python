def two_sum(nums, target):
    cache = set()
    
    for num in nums:
        delta = target - num
        if delta in cache:
            return num, delta
        cache.add(num)
    return None

def three_sum(nums, target):
    nums.sort()

    for i, num in enumerate(nums):
        subarray = nums[i+1:]
        left, right = 0, len(subarray) - 1
        delta = target - num

        while left < right:
            sum = subarray[left] + subarray[right]
            if sum == delta:
                return num, subarray[left], subarray[right]
            if sum > delta:
                right -= 1
            else:
                left += 1
    return None

