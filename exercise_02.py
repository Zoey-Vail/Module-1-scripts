# Group members:
# Aman Kumar
# Ian York
# Nikolas Bogolis
# Zoey Vail
# Gabriel Van Dreel

# Author Gabriel Van Dreel

str1 = input('Enter a string:')
str2 = input('Enter another string:')
if len(str1) > len(str2):
    if str1[0: len(str2)] == str2 or str1[-len(str2) :] == str2:
        print('True')
    else:
        print('False')
else:
    if str2[0: len(str1)] == str1 or str2[-len(str1) :] == str1:
        print('True')
    else:
        print('False')
