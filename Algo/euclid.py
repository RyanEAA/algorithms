# import math
# vars = []
# larger = 15
# smaller = 10

# print(larger%small)

# print(math.floor(larger/small))

# remainder = larger%smaller

# while(remainder!=0):
#     remainder = larger%smaller
#     larger = smaller
#     smaller = remainder
    
# print(smaller)

a = 15
b = 10

def gcd(a,b):
    if a == 0:
        return b
    
    return gcd(b&a, a)
    
print(gcd(a,b))