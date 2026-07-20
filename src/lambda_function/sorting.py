#sorting a dictionary
test_dict = {
    "ram": 33, 
    "bishnu": 44,
    "syam": 24
}

#if i iterate over test_dict then it gives only the key

for key in test_dict:
    print(key)

for key, value in test_dict.items():
    print(key, value)

# sort dict in ascending order on the basis of value
sorted_test_dict = sorted(test_dict.items(), key=lambda item: item[1])
print(test_dict)
print(sorted_test_dict)

# sort using the keys
sorted_test_dict_keys = sorted(test_dict.items(), key=lambda item: item[0])
print(sorted_test_dict_keys)

#sort keys in ascending and value in descending
num_dict = {
    1:22, 
    2:3, 
    3:41,
    4:22,
    5:1
}   
print(num_dict)

sorted_num_dict1 = sorted(num_dict.items(), key=lambda item: (item[1], -item[0]))
print(sorted_num_dict1)
sorted_num_dict2 = sorted(num_dict.items(), key=lambda item: item[0])
print(sorted_num_dict2)

#max by length

list_str = ["hello", "my", "nameis", "Pranil"]
max_word = max(list_str, key=lambda s: len(s))
print(max_word)

