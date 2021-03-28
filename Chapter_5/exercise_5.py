# common element finder function
# define a function which take 2 lists as input and return a list
# which contains common elements of both lists

# example
# input----> [1,2,5,8],[1,2,7,6]
# output---> [1,2]

def common_finder(l1,l2):
    common = []
    for i in l1:
        if i in l2:
            common.append(i)
    return common

nums1 = [1,6,5,9,8,3,4]
nums2 = [6,2,3,5,7]
print(common_finder(nums1,nums2))


