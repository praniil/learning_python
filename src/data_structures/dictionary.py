#simple dictionary can have any immutable type like string, and numbers as a key
#tuples contating immutable type like string, number can also be used as a key

simple_dict = {'jack': 4000, 'pranil': 3000, 'pranil': 200, 'pranil': 404} #should be unique key value pair, newer one replaces the same older key value pairs
print(simple_dict)

simple_dict['pranil'] = 20
print(simple_dict)

for i in simple_dict:
    if i == 'jack':
        print(simple_dict[i])

new_dict = {x: x**2 for x in [1, 2, 3, 4]}
print(new_dict)

#use key of dictionary a tuple
#simple looping technique
test_tuple1 = 'pranil', 1
test_tuple2 = 'pranil', 2
simple_dict = {test_tuple1: 40, test_tuple2: 30}
for i in simple_dict:
    if i == test_tuple1:
        print(simple_dict[i])
    
#get both the key and value pair 
dic = {"ram": 40, "pranil": 90, "rakesh": 100}
for k, v in dic.items():
    print(f"{k}: {v}")

#dic.zip()
dataset_input_set = ['hello', 'how are you', 'what is your name', 'whats your age']
dataset_output_set = ['Hi, How can i help you?', 'I am fine. Thank you!', 'My name is BotNil', 'I am 30 years old.']
# dataset = {input: output for input in dataset_input_set for output in dataset_output_set}
# print(dataset)
dataset = {input: output for input, output in zip(dataset_input_set, dataset_output_set)}
print(dataset)

for inp, out in zip(dataset_input_set, dataset_output_set):     #zip produces tuples
    print(inp, out)