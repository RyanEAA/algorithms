# find the longest subarray where there's an equal num
# of 1s and 0s

nums = [1,1,0,0,1,1,0,1,1]

class Solution():
    def contigousArray(self, arr):
        # the key will hold the sum 
        # the value will hold the index of where sum first appeared
        dict = {}
        largest_sub = []
        curr_sum = 0
        for i in range(len(arr)):
            curr_sum += (-1 if arr[i] == 0 else 1)
            #print(curr_sum)
            if curr_sum not in dict:
                # sum is getting added with the value being saved being the index
                dict[curr_sum] = i
            if curr_sum in dict:
                print(curr_sum)
                #get size of current largest sub
                if(len(arr[dict[curr_sum]: i]) > len(largest_sub)):
                    largest_sub = arr[dict[curr_sum]: i]
                    print(largest_sub)
                    print(dict[curr_sum], i)
                    print(curr_sum)
        #print(largest_sub)
        #print(dict)
        
        
        
        
print(Solution().contigousArray(nums))
        