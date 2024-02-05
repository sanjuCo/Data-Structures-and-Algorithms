""" 
It is better to have a comment here mentioning the question (problem you are solb=ving and explaining your solution
"""
"""
Please place comments about the running time of your solution
"""

"""
Avoid using default programming language functions like reverese. The aim of this task is to implement the reverse function
"""
def rotate(nums, k):
    n=len(nums)
    k %=n

    nums.reverse()

    nums[:k] = reversed(nums[:k])

    nums[k:] = reversed(nums[k:])
