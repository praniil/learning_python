any_set = {"monkey", "donkey", "monkey", 1, True}
print(any_set)
print(type(any_set))

for i in any_set:
    if i == "monkey":
        print("monkey spotted")

a = set('abcdefabsc')
print(a)
arbitrary_set = {x for x in a if x not in 'abc'}
print(arbitrary_set)

#set is not ordered i.e. it can show result in random order
#set always have unique item

test_set = {1, 2, 3, 4, 5, 6, 4, 5}
print(test_set)

# print(test_set[0]) error

#set operation
a_test = set('abcdefghijklzkabs')
b_test = set('abc')
print("a_test: ", a_test)
print("b_test: ", b_test)
print(a_test - b_test)
print(a_test & b_test)
print(a_test | b_test)
print(a_test ^ b_test)

