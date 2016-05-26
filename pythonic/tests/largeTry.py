""" This code is not pythonic """

try:
    print "This will be a large try"
    print "This code is horrible"
    bar = foo * 3 # Raise NameError
    foobar = 10/0 # Raise ZeroDivisionError
    print 'two: ' + 2  # Raise TypeError
    print foobar
except Exception as e:
    print e
finally:
    print "I'm in finally clause"
