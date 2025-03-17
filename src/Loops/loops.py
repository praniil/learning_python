from typing import List
def add(a, b):
    return a+b

def odd_even(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

def primeNumber(n: List[int]):
    for prime in n:                 #n:= list of prime integers, for prime in n: prime is each element in the list
        print(prime)

