def remove_duplicates(nums):
        
        i, j = 0, 1
        
        n = len(nums)
        
        while i < n-1:
            while nums[i] == nums[j]:
                el = nums[i]
                nums.remove(el)
                n -= 1
                if n == 1 or j > n-1:
                    break
        
            i += 1
            j = i + 1
            
        return nums
