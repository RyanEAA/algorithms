#Given an array of positive integers, find the subarrays that add up to a given number
#sub array can be any size as long at the target is matched
# it's important to remember that subarray are contigous
# time complexity of O(n)
# space complexity of O(n) bc it the worst case scenerio the whole array will be sevens

#using a brute force approach is no ideal because it
#input size can be anything and the memory will be exceeded

nums = [1,7,4,3,1,2,1,5,1]
target = 7

class Solution():
    def findSubArrays(self, array, target):
        l = 0
        r = 0
        list_of_subs = []
        while(r <= len(array)):
            #print(array[l:r])
            
            if(sum(array[l:r]) == target):
                list_of_subs.append(array[l:r])
            
            if(sum(array[l:r]) <= target):
                r += 1
            
            if(sum(array[l:r]) > target):
                l+=1
        return list_of_subs
                
        
print(Solution().findSubArrays(nums, target))