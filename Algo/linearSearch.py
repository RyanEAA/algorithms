def search(arr, x):
    
    for i in range(len(arr)): #for every element in the array
        if arr[i] == x: #if the element is equal to the target
            return i
        
    return -1 #if the target is not in the array


arr = [10,20,80,30,60,50,110,100,130,170]

x = 175

print("POS OF X: ", search(arr,x))