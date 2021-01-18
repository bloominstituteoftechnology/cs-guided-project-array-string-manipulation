"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.
​
The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.
​
If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.
​
Example 1:
​
Input: nums = [1,7,  3,  6,5,6]
Output: 3       8          17
              
              [1,7,3,   6,   5,6]
                11            11
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.
​
Example 2:
​
Input: nums = [1,2, 3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
def pivot_index(nums):
    # Your code here
    '''
    Input: List of integers 
    Output: an int, the pivot index (note that we don't count the value at the pivot)
​
    Plan 1: Loop through each number
            Get the sum of all numbers to this number's left side 
            Get the sum of all numbers to this number's right side 
            If the two sums match, return the index of the current number 
​
    This plan works, but we perform a lot of redundant summing 
    Because of the fact that we're touching every other number except the 
    current number, for every single number in the list, this is an O(n^2) 
    solution 
​
    Plan 2: keep track of the total sum of the list 
            keep track of the current running sum as we iterate 
            iterate through our numbers 
            subtract the current number from the total 
            check if the new total == running sum 
                if it does, return the index of the current number 
                else, add the current number to the running sum 
            if we reach the end of the loop, then no number satisfies
            what we're looking for, so return -1 
​
    For this plan, when iterating, we only take the current number and 
    add/subtract it from a variable we're keeping track of
    So when iterating, we only look at the current number, and none of the 
    other numbers in the list 
    '''
    # O(n) + O(n) == O(2 * n) ~ O(n) time 
    # O(1) space 

#     total = sum(nums) # O(n)
#     running = 0 
# ​
#     for i, num in enumerate(nums): # O(n)
#         # O(1)
#         # subtract num from total 
#         total -= num
# ​
#         # check if total == running 
#         if total == running:
#             # return the index of num 
#             return i
# ​
#         running += num
# ​
#     return -1
# ​
# ​
# nums = [1,2,3]
# print(pivot_index(nums))

#     for i in range(len(nums)):
#         left_subarray = nums[0:i]
#         right_subarray = nums[i + 1:]
#         left_sum = sum(left_subarray)
#         right_sum = sum(right_subarray)
#         if left_sum == right_sum:
#             return i
#     return - 1
    

# print(pivot_index([1,7,3,6,5,6]))
#     l_sum = 0
#     r_sum = sum(nums[1:])
#     for i in range(len(nums)):
#         if l_sum == r_sum:
#             return i
#         l_sum += nums[i]
#         if (i + 1 == len(nums)):
#             r_sum = 0
#         else:
#             r_sum -= nums[i+1]
#     return -1
# print(pivot_index([1,7,3,6,5,6]))
    total_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1


print(pivot_index([1,7,3,6,5,6]))