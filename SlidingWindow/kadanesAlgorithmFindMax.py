
nums = [-2,-3, 4, -1, -2, 1, 5, -3]

class Solution():
    def kadanesAlgoFindMax(self, arr):
        
        current_max = 0
        current_sum = 0
        
        for i in range(len(arr)):
            current_sum += arr[i]
            # print(current_sum,"currsom")
            # print(current_max, "currmax")
            
            if(current_sum > current_max):
                current_max = current_sum
            
            
            if(current_sum < 0):
                current_sum = 0 # resets current sum
        
        return current_max
    
print(Solution().kadanesAlgoFindMax(nums))
            
            
                
            
        