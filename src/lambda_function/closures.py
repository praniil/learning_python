def multiplier_func(number):

    def multiply(factor):
        return number * factor
    return multiply

mul = multiplier_func(5)
print(mul(3))
            