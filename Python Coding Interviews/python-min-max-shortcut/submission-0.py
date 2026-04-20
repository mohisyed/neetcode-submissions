from typing import List


def disallow_negatives(num: int) -> int:
    # min >= 0 
    num = max(num, 0)
    if num >= 0:
        return num
    return 0


def max_difference(nums: List[int]) -> int:
    temp_min = -1
    temp_max = -1
    for i in range(1,len(nums)):
        temp_distance = nums[i] - nums[i-1]
        temp_max = max(temp_max, temp_distance)
    return temp_max




# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
