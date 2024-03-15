# kaden's algorithm to sub the sub array that add up to the largest sum
# really beautiful algorithm using the sliding windows technique

nums = [-2,-3, 4, -1, -2, 1, 5, -3]

class Solution():
    def kadensAlgoLargSumSub(self, arr):
        
        lar_sub = []
        
        
        l = 0
        r = 1
        
        #curr_sub = arr[l:r]
        
        while r <= len(arr):
            curr_sub = arr[l:r]
            #print(curr_sub)
            
            if (sum(curr_sub) > sum(lar_sub)):
                #print(curr_sub)
                lar_sub = curr_sub
                
            if(sum(curr_sub) < 0):
                l += 1
                r += 1
            
            r+=1
            
        return lar_sub, l, r

#sub_sol, l_ind, r_index = 
print(Solution().kadensAlgoLargSumSub(nums))
        
        