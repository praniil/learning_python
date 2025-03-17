# import numpy as np
from collections import deque

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

#test
test_list = [1, 2, 3, 4, 5]
print(test_list[:])
print(test_list[:len(test_list)])
print(test_list[:-1])

#list.count(x) counts the number of x in the list
count_list = [1, 2, 1, 2, 3, 4, 1]
print(count_list.count(1))
print(count_list.count(2))

#list.reverse()
lsit = ["Prnail", "Parajuli"]
lsit.reverse()
print(lsit)

#copy list.copy
og_list = [1, 2, 3, 4, 5]
copy_list = og_list.copy()
print(id(og_list) == id(copy_list)) #gives false

copy_list[:] = [1, 2]
print(og_list)  #doesnt change because it is shallow copy
print(copy_list)

#list.sort()
def my_func(e):
    return len(e) 

non_sorted = [33, 42, 12, 100, 43, 1]
non_sorted.sort(reverse=True)
print(non_sorted)
non_sorted.sort()
print(non_sorted)

non_sorted_string = ["car", "donkey", "kathmandu"]
non_sorted_string.sort(reverse=False, key=my_func)  #key specifies the criteria
print(non_sorted_string)

#list.index(x[, start[, end]])
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'banana', 'apple', 'banana']
search_index = fruits.index('banana', 4)    #find next banana starting at position 4
print(search_index)

#list as a stack
stack = [1, 2, 3, 4]
stack.append(5)
print(stack)
stack.pop()
print(stack)

#list as a queue
queue = deque(["pranil", "nil", "is"])
queue.append("goat")
print(queue)
queue.popleft()
print(queue)

#list comprehension
old_list = [1, 2, 3, 4, 5]
new_list = []
for i23 in old_list:
    new_list.append(i23**2)

print("new_list: ", new_list)
print(i23)  #i23 is still available here after the for loop ends wtffff

#side effect like i23 is not seen
new_list2 = [x23**2 for x23 in old_list]
print("new_list2: ", new_list2) 

less_than_list = []
less_than_list.append(set((x, y) for x in [1, 2, 3] for y in [5, 6, 7] if x < y))
print(less_than_list)

num_and_square = []
print(list((x, x**2) for x in range(5)))
num_and_square.append(list((x, x**2) for x in range(5)))
print(num_and_square)


#del a[0]
del_list = [1, 2, 3, 4, 5]
del del_list[0]
print(del_list)

#testing something
testing_list = [(a, b) for a in [1, 2, 3] for b in [5, 6, 7] if a < b]
print(testing_list)

testing_list2 = []
testing_list2.append([(a, b) for a in [1, 2, 3] for b in [5, 6, 7] if a < b])
print("testing list", testing_list2)

#iterate through list
iter_list = [1, 2, 3, 4, "pranil"]
for i in iter_list:
    print(i) #gives the item not the index

for (i, v) in enumerate(iter_list):
    print(f"iter_list[{i}] = {v}")