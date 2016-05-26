def createSquares(untilNum):
    list = range(untilNum+1)
    for i in list:
        yield i**2

squaresUntil10 = createSquares(10)

for i in squaresUntil10:
    print i
