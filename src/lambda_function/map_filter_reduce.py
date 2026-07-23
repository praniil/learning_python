def greet():
    return "hello"
#greet is a func object
# everything in apython is an object
say_hello = greet
print(say_hello())

#sending and returning the function 
# this is called high order funciton in python
def returntrue(func):
    return func()

def result():
    return True

res = returntrue(result)
print(res)

#map
nums = [1, 2, 3]
mapped = {}

print(list(map(lambda x: x**2, nums)))

words = ["hello", "worlds"]
max_len_word = max(words, key=lambda word: len(word))
print(max_len_word)