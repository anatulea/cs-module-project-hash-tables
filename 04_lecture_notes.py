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