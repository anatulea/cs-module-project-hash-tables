# birthday paradox
import random
import hashlib

def our_hash_func(key, num_buckets):
    key_bites = f'{key}'.encode()
    hashed_key = int(hashlib.sha3_256(key_bites).hexdigest(),16)
    return hashed_key % num_buckets # produces always a unique output, but we mod it's output , so we wil have collisions

def how_many_before_collision(num_buckets):

    hash_keys =set()
    tries = 0

    while True:
        key = random.random()
        hashed_key = our_hash_func(key, num_buckets)
        if hashed_key in hash_keys:
            break
        else:
            hash_keys.add(hashed_key)
            tries +=1 
    return tries
print(how_many_before_collision(10330))




# memoization, closely related to dynamic programming
## DP: top down, break the problem up as you
## reuse previous results
## key is what you have, value is what you calculate 

# fibonacci sequence
## a function that returns the n-th item in the fibonacci sequence
## golden proportion

## 0 1 1 2 3 5 8 13 21 34 55 89
### Kanban board: card holds a feature, "make this button"
### 1 2 3 5 8 13 21 

# let's do it recursively

# need base case
# progress toward base case

cache = {}
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

print(fib(3)) # should be 2
print(fib(6)) # should be 8
print(fib(11)) # should be 89


# expensive calculation on the fly
import math

lookup_table = {}

def inverse_root(n):
    return 1/math.sqrt(n)

for i in range(1, 1000):
    lookup_table[i] = inverse_root(i)

print(lookup_table[995])

# rainbow table
## hash common passwords ahead of time
## precomputed table for caching the output of cryptographic hash functions,
# usually for cracking password hashes

# hashing function for pws should be slow
