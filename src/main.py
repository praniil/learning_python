import Loops
from Loops.loops import add, odd_even, primeNumber
# primes = [2, 3, 5, 7]
# primeNumber(primes)
# print(add(2, 3))

n = 5
for i in range(n):
    if i % 2 == 0 :
        print("even")
    else:
        print("odd")

sum_even= 0
sum_odd = 0
for j in range(n):
    if j % 2 == 0:
        sum_even = sum_even + j
    else:
        sum_odd = sum_odd + j
    
print("the sum of even number is %d" %sum_even)
print("the sum of odd number is %d" %sum_odd)