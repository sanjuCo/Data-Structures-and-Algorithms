""" 
It is better to have a comment here mentioning the question (problem you are solb=ving and explaining your solution
"""
"""
Please place comments about the running time of your solution
"""
def Duplicate(nums):
    n = set()

    for num in nums:

        if num in n:
            return True
        else:
             n.add(num)
        
    return False # Looks like you are always retruning False in this function
