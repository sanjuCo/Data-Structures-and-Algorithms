""" 
It is better to have a comment here mentioning the question (problem you are solb=ving and explaining your solution
"""
"""
Please place comments about the running time of your solution
"""
"""
WRONG SOLUTION, CAN YOU READ THE QUESTION AGAIN.
"""
"""
The problem is: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
"""

def singleNumber(nums):
    
    number = 0
    for num in nums:
        number ^=num

    return number
