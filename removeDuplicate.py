""" 
It is better to have a comment here mentioning the question (problem you are solb=ving and explaining your solution
"""
"""
Looks like you have a WRONG SOLUTION; Can you try your solution with the following array:
[29,2,4,7,29,3,11,40,29,2,10,60]
Please place comments about the running time of your solution
"""
def remove_duplicates(nums):
    if not nums: # Very good
        return 0
    
    i = 0

    for j in range(1, len(nums)):

        if nums[j] != nums[i]:
        
            # Move the pointer forward
            i += 1

            # Update the element at the new position
            nums[i] = nums[j]
            
    return i + 1 # Why are we returning this? I would imagine this should be a list (i.e. a list without the duplicates)
