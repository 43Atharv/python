nums=[1,4,9,16,25,36,49,86,81,100]

x = 36

i=0
while i < len(nums):
    if(nums[i]==x):
        print("found at idx:",i)
        break
        
    else:
        print("not found")
    i += 1         
    