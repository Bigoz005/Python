from array import *

my_array = array('i', [1, 1, 2, 2, 2, 4, 5, 6, 7, 8])

for j in [0, 2, 4, 6, 8]:

    if my_array[j] == my_array[j + 1]:
        print(my_array[j], my_array[j + 1])
        print("dobra para")

    else:
        print(my_array[j], my_array[j + 1])
        print("zla para")

