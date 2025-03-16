# import numpy as np

list1 = {1, 2, 3, 'a', 'b', 'c', 1}
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

# my_list1.append(np.array(2, 3))
my_list1.append([2, 3])
print(my_list1)
my_list1.append(23)
print(my_list1)

for i in range(len(my_list1)):
    print(my_list1[i])

#append a list
animals = ['cheeta', 'dog', 'cat']
animals[len(animals):] = ['tiger', 'crocodile']
print(animals)
animals[1: 3] = ['human', 'whale', 'donkey', 'monkey']
print(animals)

#give me the third and forth value of list animals
x = slice(2, 5) #first-> start posn (includes it) #last5 -> finish posn (excludes it)
print(animals[x])

x1 = slice(1, 5, 2) #last element is tuple i.e. 2 is the step of slicing 
print(animals[x1])

#list.extend(iterable) Any iterable (list, set, tuple, etc.)
any_list = [1, 2, 3, 4, 5]
any_set = {"apple", "banana", "carrot"}
any_tuple = (True, False)

any_list.extend(any_set)
print(any_list)
any_list.extend(any_tuple)
print(any_list)

for i in any_list:
    print(i)

#list.insert(i, x)  insert x in the ith position and shifts the positon of other items in the list one step back
new_list = [1, 2 , 3, 'a', 'b', 'c']
print(len(new_list))
new_list.insert(0, 'pranil')
print(new_list)
print(len(new_list))

#list.remove(x) removes x from the list
rem_list = [1, 2, 3, 4, 'pranil', 5]
rem_list.remove(1)
print(rem_list)
rem_list.remove('pranil')
print(rem_list)

#list.pop([i])
pop_list = [1, 2, 3, 4, 5, 6]
popped_item = pop_list.pop(len(pop_list) - 1) #should pop last item
print("1: ", popped_item)
print(pop_list)
popped_item2 = pop_list.pop(len(pop_list) - 2) #should pop secondlast item
print(popped_item2)
popped_item3 = pop_list.pop() #no index mentioned -> pops the last item
print(popped_item3)

#list.clear() #clears the list, give the empty list []
list_clear = [1, 3, 4, 4, 5]
list_clear.clear()
print("clear1", list_clear)

another_way = [1, 2, 3, 4, 5]
another_way[:] = []
print("clear2", another_way)
