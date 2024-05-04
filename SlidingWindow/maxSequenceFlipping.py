# given an array of 0s and 1s find the largeset suba
# find subarray with equal number of 0s and 1s 
# by flipping at most k 0 and 1s

nums = [1, 0 , 1, 1, 1 , 0, 0]
target = 0
class Solution():
    def flip(self, array, target):
        l = 0
        r = 0
        list_of_subs = []
        new_arr = [-1  if x == 1 else 0 for  x in array]
        
        while(r <= len(array)):
            #print(array[l:r])
            
            if(sum(array[l:r]) == target):
                list_of_subs.append(array[l:r])
            
            if(sum(array[l:r]) <= target):
                r += 1
            
            if(sum(array[l:r]) > target):
                l+=1
        return list_of_subs
                 
                
                
print(Solution().flip(nums, target))       