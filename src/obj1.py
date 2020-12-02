# describe the difference between in-place and out-of-place algorithms 
# x = []
# n = [1, 2, 3]
# def tripple_in_place(nums): # O(n), O(1)
#     for index in range(len(nums)):
#         # nums[index] = nums[index] * 3
#         nums[index] *= 3
# ​
# print(n)
# x = tripple_in_place(n)
# print(n)
# ​
# print(x)



xx = []
n = [1, 2, 3]
def tripple_out_place(nums): # O(n), O(n)
    new_nums = [None] * len(nums)
    for index in range(len(nums)):
        # nums[index] = nums[index] * 3
        new_nums[index] = nums[index] * 3
    
    return new_nums
print(x)
print(n)
x = tripple_out_place(n)
print(n)
print(x)