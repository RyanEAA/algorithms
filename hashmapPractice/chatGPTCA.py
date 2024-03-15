nums = [1,1,0,0,1,1,0,1,1]

class Solution():
    def contiguousArray(self, arr):
        # the key will hold the sum 
        # the value will hold the index of where sum first appeared
        my_dict = {}
        largest_sub = []
        curr_sum = 0
        for i in range(len(arr)):
            curr_sum += (-1 if arr[i] == 0 else 1)
            if curr_sum not in my_dict:
                # sum is getting added with the value being saved being the index
                my_dict[curr_sum] = i
            else:
                # Found a subarray with the same sum, check if it's the largest
                sub_len = i - my_dict[curr_sum]
                if sub_len > len(largest_sub):
                    largest_sub = arr[my_dict[curr_sum] + 1: i + 1]
        return largest_sub
        
print(Solution().contiguousArray(nums))
