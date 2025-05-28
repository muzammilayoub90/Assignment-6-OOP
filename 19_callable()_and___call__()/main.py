class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return self.factor * number
    
triple = Multiplier(3)
print(callable(triple))

result = triple(10)
3 * 10
print(result)