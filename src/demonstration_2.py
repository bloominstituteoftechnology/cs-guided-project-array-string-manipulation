"""
You are given a non-empty array that represents the digits of a non-negative integer.
​
Write a function that increments the number by 1.
​
The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.
​
You will not receive a leading 0 in your input array (except for the number 0 itself).
​
Example 1:
​
Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.
​
Example 2:
​
Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.
​
Example 3:
​
Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""


Here's the code we wrote for the plus_one problem.
To explain a bit more why the digits.insert() call is O(n) time, this how to do with how lists are laid out in memory. For example, if we have a list such as [3, 1, 2] and we want to insert a 4 at the beginning of this list to get [4, 3, 1, 2], how is that done under the hood?
Because of the fact that we expect that the inserted 4 will be at index 0 after the insertion, this means that the 3 has to be moved to index 1, the 1 has to be moved to index 2, and the 2 has to be moved to index 3. This all has to happen so that the slot at index 0 is available for us to park the 4 there.
To illustrate this, here's the starting state of our list, with indices to denote where each element is:
  0  1  2  
[ 3, 1, 2]
Again, we need to make space for the 4 at index 0, so in order to do that, our list is updated so that it looks like this (where the _ is denoting where the 4 will go):
  0  1  2  3
[ _, 3, 1, 2 ]
Now there's space for us to park the 4 at index 0, so we end up with the final state of our list:
  0  1  2  3
[ 4, 3, 1, 2 ]
The TL;DR here is that, when adding an element anywhere except the back of the list (using append / push methods), the runtime for such an operation is worst case O(n), due to the fact that we need to shift every element after the spot we want to insert into over by 1 spot. This is necessary because we have to make room for the new element we want to insert.




def plus_one(digits):
    # Your code here
    '''
    Input: List of integer digits 
    Output: List of integer digits representing the original number + 1 
​
    Plan 1: Transform it into a single integer
                - Join the list of integers into a single string 
                - Change the single string into an integer with the `int` function
            Add one to our transformed integer (this takes care of carrying for us)
            Transform the integer back into a list of digits 
​
    Plan 2: Can we re-use the input to do what we want to do? 
            Can we just act on the input `digits` list?
            [1,3,2] + 1: add 1 to the last element in the list 
            When the last list element != 9, add 1 to it 
            When the last list element == 9, we have to think about how 
            to perform carry-over 
            [9,9,9] + 1
            
            Recreate the process by which we would do this with pencil and paper
            If the last element is a 9, change it to a 0, and then carry over 
            by iterating right to left 
            Keep iterating so long as we see 9's
            If we get all the through the list, and we only saw 9's, then we 
            add a 1 to the front of our list 
​
            Time complexity: Worst case, we're given nothing but 9's, meaning
            we have to iterate over the entire list, O(n)
​
            Space complexity: Since we're re-using our input list, this is 
            constant, O(1) 
    '''
​
    # iterate in reverse 
    for i in range(len(digits)-1, -1, -1):
        # check if the current digit == 9 
        if digits[i] != 9:
            digits[i] += 1
            # we're done; return our result 
            return digits
​
        # otherwise, the current digit is 9 
        digits[i] = 0 
        
    # if we reach outside of this for loop, then we got nothing but 9's 
    # we need to add a 1 to the front of our list 
    # Can be O(n) space in rare cases, but generally doesn't happen enough for us 
    # to consider it 
    # It is O(n) time complexity 
    digits.insert(0, 1) 
​
    return digits
​
print(plus_one([9,9])