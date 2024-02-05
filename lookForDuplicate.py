""" 
It is better to have a comment here mentioning the question (problem you are solb=ving and explaining your solution
"""
"""
Please place comments about the running time of your solution
"""
"""
The time complexity of this is O(n) where n is the number of elements in the array
"""
def Duplicate(nums):
    n = set()

    for num in nums:

        if num in n:
            return True
        else:
             n.add(num)
        
    return False # Looks like you are always retruning False in this function

#The function will only return False after the for loop and no duplicate is found because the return False statement is indented to the scope of the function itself
