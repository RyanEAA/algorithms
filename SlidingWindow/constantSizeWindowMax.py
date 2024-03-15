#find the maximum sum sub array of required size
# time complexity o(n)
# space complexity o(1)
# can be used for finding minimum

#makes it better than the simple brute force approach



#important to remember is that subarray are contigous

nums = [-1, 2, 3, 1, -3, 2]

class Solution():
    def slidingWindow(self, array, size):
        
        l = 0
        r = size
        current_max = 0
        while (r <= len(array)):
            print(array[l:r])
            if(sum(array[l:r]) > current_max):
                current_max = sum(array[l:r])
            l += 1
            r += 1
            
        return current_max
            
print(Solution().slidingWindow(nums, 2))