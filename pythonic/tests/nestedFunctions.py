def makeMultiplicateBy(num1):
    def multiplyTo(num2):
        return num1 * num2
    return multiply

double = makeMultiplicateBy(2)

print double(4)
