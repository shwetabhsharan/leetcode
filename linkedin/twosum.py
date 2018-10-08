def two_sum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            print nums[i], nums[j]
            if target == nums[i] + nums[j]:
                return [i, j]

# two_sum([2, 7, 11, 15], 9)

def two_sum_dict(nums, target):
    data_dict = {}
    for i in range(0, len(nums)):
        diff = target-nums[i]
        if diff in data_dict:
            return [i, data_dict[diff]]
        data_dict[nums[i]] = i

print two_sum_dict([2, 7, 11, 15], 9)