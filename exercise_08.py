# Group members:
# Aman Kumar
# Ian York
# Nikolas Bogolis
# Zoey Vail
# Gabriel Van Dreel

# Author Zoey Vail
arr = []
for i in range(10):
    arr.append(input('Enter number '+ str(i + 1) + ':'))
check = True
newArr = []
for i in range(10):
    check = True 
    for r in range(10):
        if r > i and arr[i] == arr[r]:
            check = False
            break
        if r < i and arr[i] == arr[r]:
            check = False
            break
    if check == True:
        newArr.append(arr[i])    
print('Original list:', arr)
print('Numbers that appear once:', newArr)


    