"""
Code obtained from http://www.secnetix.de/olli/Python/lambda_functions.hawk
Compute prime numbers in python
"""
nums = range(2, 50)
for i in range(2, 8):
    nums = filter(lambda x: x == i or x % i, nums)
print nums
