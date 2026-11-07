from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    total_sum = 0
    for x in nums:
        total_sum += x

    return total_sum

def get_min(nums: List[int]) -> int:
    min_val = float('inf')
    for x in nums:
        if x < min_val:
            min_val = x
    return min_val

def get_max(nums: List[int]) -> int:
    max_val = float('-inf')
    for x in nums:
        if x > max_val:
            max_val = x
    return max_val

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
