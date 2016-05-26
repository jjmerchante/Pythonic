squares = map(lambda x: x**2, range(10))
div_3or5 = filter(lambda x: x%3 == 0 or x%5 == 0, range(10))
sumTo10 = reduce(lambda x, y: x+y, range(11))
