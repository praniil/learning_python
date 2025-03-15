import numpy as np

list1 = {1, 2, 3, 'a', 'b', 'c'}
list1.remove(2)
print(list1)

rgb = ["red", "green", "blue"]
print(id(rgb))  #object memory's address

rgba = rgb
print(hex(id(rgb))) #address of the list rgb
print(id(rgba))     #address of the list rgba

print(id(rgba) == id(rgb))  #should return true (reference the same object)

rgba.append("Alpha")
print(rgb)

#replace the items of the list
my_list = [1, 2, 3, 'a', 'b', 'c', 4, 5, 6]
my_list[2:4] = ['x', 'y']
# print(my_list)
# my_list[:] = []
# print(len(my_list))

#using loop
for i in range(len(my_list)):
    my_list[i] = i

print(my_list)

#nested list
my_list1 = [[1, 2, 3], ['a', 'ad', 'x']]
print(my_list1)

my_list1.append(np.array(2, 3))