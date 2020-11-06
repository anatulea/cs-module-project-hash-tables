"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)
from itertools import product
def f(x):
    return x * 4 + 6

# Your code here
cache ={}
def findcombinations(q):
    nums = list(product(q, repeat = 4))
    # print(nums)
    for a,b,c,d in nums:
        mysum = f(a)+ f(b)
        mysub = f(c) - f(d)
        if mysum == mysub: 
            if mysum not in cache:
                cache[mysum] = [[a,b, c, d]]
            else:
                cache[mysum] = list(cache[mysum]+ [[a, b, c, d]])
            
    return cache
q2 = (1, 3, 4, 7, 12)
print(findcombinations(q2))