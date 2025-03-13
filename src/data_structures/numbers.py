a = 20
b = 15
print(a / b)    #a and b are int but the division result is always float
print(a // b) #gives the floor value
print(a ** b) #a to the power b

#raw string => a special type of string that allows you to include backslashes ( \ ) without interpreting them as escape sequences
print('C:\some\name')
print(r'C:\some\name')

print('''#
Yoo dude
        How u doin
''')

#Strings can be concatenated (glued together) with the + operator, and repeated with *:
print(3 * 'un' + 'able')

#Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
print('hello ' 'boy')
print('hello my name is: ' 'A boy')

#position -1 means last element
word = 'Python'
print(word[-1])
print(word[-2])
print(word[-3])

sentence = 'My name is Pranil and i am awesome'
print(sentence[:])  #prints all from the Position 0 included upto last position included

print(sentence[:4]) #4th position excluded

new_word = 'Golang'
print(new_word[0:2])    #position 0 included 2 exluded
print(new_word[2:5])
print(new_word[:5])
print(new_word[2:])     #position 2 included last included
print(new_word[-2:])
