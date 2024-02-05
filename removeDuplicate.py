def remove_duplicates(nums):
    if not nums:
        return 0
    
    i = 0

    for j in range(1, len(nums)):

        if nums[j] != nums[i]:
        
            # Move the pointer forward
            i += 1

            # Update the element at the new position
            nums[i] = nums[j]
            
    return i + 1