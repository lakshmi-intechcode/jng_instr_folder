'''
think about how this could be improved...
for example, after the first pass through the loop
99 will be at the right end of the list. Is there some way
I could keep track of this, and know that 99 is in the correct
position after the first iteration? That way, I wouldn't have
to check it again on each subsequent iteration.
'''
import pudb
def bubble_sort(my_list):
    pu.db
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(my_list)-1):
            if my_list[i] > my_list[i + 1]:
                temp = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = temp
                swapped = True
    return my_list

bubble_sort([5,19,4,1,36,99,2])
# assert bubble_sort([5,19,4,1,36,99,2]) == sorted([5,19,4,1,36,99,2])
# assert bubble_sort(["Greg", "Armen", "Ken"]) == sorted(["Greg", "Armen", "Ken"])
# unsorted = [101, 259, 76, 265, 298, 245, 44, 297, 142, 50, 95, 153, 158, 38, 149, 25, 96, 238, 124, 67, 244, 118, 154, 190, 98, 41, 0, 86, 102, 3, 172, 109, 257, 238, 166, 19, 72, 220, 30, 29, 283, 199, 191, 112, 266, 169, 273, 168, 193, 76, 17, 6, 270, 162, 282, 237, 246, 20, 18, 174, 296, 99, 25, 128, 88, 149, 255, 229, 155, 149, 85, 252, 19, 185, 50, 1, 280, 194, 87, 58, 203, 18, 286, 271, 172, 196, 107, 77, 37, 175, 1, 127, 77, 2, 156, 62, 204, 287, 238, 49, 260, 205, 13, 6, 20, 74, 204, 203, 192, 218, 269, 36, 219, 144, 5, 34, 165, 163, 60, 117, 222, 139, 243, 179, 149, 245, 34, 5, 0, 3, 255, 150, 45, 60, 54, 52, 86, 182, 286, 221, 138, 187, 187, 233, 5, 47, 88, 243, 92, 43, 79, 89, 214, 52, 91, 50, 297, 75, 178, 194, 282, 253, 269, 218, 221, 69, 213, 113, 281, 294, 29, 62, 250, 91, 56, 113, 13, 47, 116, 116, 61, 92, 112, 27, 52, 144, 45, 127, 213, 119, 135, 66, 145, 165, 283, 246, 48, 83, 131, 73, 183, 211, 6, 96, 104, 246, 211, 155, 265, 159, 124, 27, 267, 238, 292, 32, 276, 222, 292, 298, 96, 34, 158, 102, 241, 116, 69, 102, 291, 261, 15, 214, 17, 268, 26, 254, 103, 39, 9, 164, 234, 106, 74, 30, 3, 102, 105, 27]
# assert bubble_sort(unsorted) == sorted(unsorted)
# assert bubble_sort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]
