# does a hash table preserve order?

"""
hash_table = HashTable()

hash_table.storage = [Node('key3', 'v3'), None, None, Node('key1', 'v1')]

hash_table.put('key1', 'v1')
hash_table.put('key2', 'v2')
hash_table.put('key3', 'v3')

hash_table.storage.sort()

hash_table.get('key1')
"""

# hash the key, get the index, looks there...????

arr = [1, 2, 3]
arr.append(1)
arr.append(2)
arr.append(3)

# why doesn't a hash table keep things in order, the way an array does?
# the hash function takes the key and returns a random index

# sets, dictionaries, object or hash maps

# can you sort a hash table (or dictionary/object/hash map)?
# go to the index, sort the linked list?

arr.sort()

# in Python, what if we got a list based on the dictionary?
my_dict = {
    'a': '1',
    'f00': 'izzy',
    'qux': 'bar',
}
# a list-like object - actually an iterator
my_dict.items()

dict_list = list(my_dict.items())

# sort by default goes in ascending order, aka normal alphabetical
# also by default uses the first item in each tuple to sort

dict_list.sort(reverse=True)

print(dict_list)

# print in ascending order, sorted by value
dict_list.sort(key=lambda tuple_pair: tuple_pair[1])
print(dict_list)

"""
[('a', 1), ('f00', 'bar'), ('qux', 'izzy')]


JS
x => x * x

lambda x, y: x * y

HOF: a function that takes a function
in functional programming (FP), we don't work in place
Instead always returns a new data structure

"pure function" has no side effects

map(lambda x: x * 2, [1, 2, 3, 4])
<map object at 0x10a5f8e10>
list(map(lambda x: x * 2, [1, 2, 3, 4]))
[2, 4, 6, 8]
"""

# given a string, count how many times each letter occurs in it
# print by descending order, from the most common letter to the least common

our_string = 'supercalifragilisticexpialidocious'


# UPER
# Understand
# What about spaces and special chars?
# ignore for now, just count alphabet letters

# Plan
# loop and place in a dict
# use our Python list sorting methods to sort by descending order of the values not keys

# E

def letter_count(s):
    our_dict = {}

    for letter in s:
        if letter in our_dict:
            our_dict[letter] += 1

        else:
            # ignore non-alphabetic characters
            if letter.isalpha():
                our_dict[letter] = 1
         
    return our_dict

count_dict = letter_count(our_string)

list_dict = list(count_dict.items())

list_dict.sort(reverse=True, key=lambda pair: pair[1])
# sorted()

v_set = set()
for k, v in list_dict:
    if v not in v_set:
        print(v, k)
        v_set.add(v)
    else:
        print(' ', k)



# stretch goal from Omid: print each v only once
# or do we want them all on one line, comma-separated?

records = [
    ("Tara", "Web"),
    ("Kyle", "Web"),
    ("Adrian", "Web"),
    ("Janessa", "Web"),
    ("Mike", "Web"),
    ("Cai", "DS"),
    ("Chris", "DS"),
    ("Craig", "iOS")
]

# how could we show in O(1) time everyone in a particular track?

# build an index, or indexing on an attribute

# index on the track: make the track the key, have as value a list, append the names to the list

def build_index(records):
    idx = {}
    for name, track in records:
        if track in idx:
            idx[track].append(name)

        else:
            idx[track] = [name]

    return idx

# index the data on an attribute: rooms in a house, pools

indexed_records = build_index(records)

print(indexed_records['DS'])
print(indexed_records['Web'])
print(indexed_records['iOS'])




# transposition table

# you have data to transform from one form into another

# transposition cipher
# Caesar cipher --> 'rotate' the letter

# given a string, build a new string by looking up each letter

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

# make a function to encode a string
# iterate through the string we're given
# for every letter, look up its encoding (its transformation)
# build a new string

first_string = 'hello'

def encode(old_string):
    new_string = ''

    for letter in old_string.upper():
        new_string = new_string + encode_table[letter]

    return new_string

herrow = encode(first_string)
print(herrow)

# make a decode table so we can also decode our super secret messages
# with encode table, keys --> values, values --> keys

## iterate through encode table
### for each key, value, add to a new dictionary with value, key
decode_table = {}
for key, value in encode_table.items():
    decode_table[value] = key


def decode(old_string):
    new_string = ''

    for letter in old_string.upper():
        new_string = new_string + decode_table[letter]

    return new_string

decoded = decode(herrow)
print(decoded)






# Web client cache

# "client" gets whatever URL we provide

# this client should cache the web page

# on first request, the client fetches the web page
# on subsequent requests, the client gives you what it previously fetched

# why?
## speed
### especially for large pages or on a slow connection

## avoid database hits
### don't overpay for services
### countries that charge by download

# how to use hash tables to create a web client cache?
## (aka proxy server)

## what should be the key, what should be the value?
### value: the returned HTML/JS/CSS - the dom
### key: fetch date?, or URL

# thefacebook.com, google.com

import urllib.request

cache = {}
def web_client(URL):

    # check if the URL is in cache
    if URL in cache:
        print('found locally, saving time!!')
        return cache[URL]

    # otherwise, fetch and put in cache
    else:
        print("did not find, going out over the interwebs")
        response = urllib.request.urlopen(URL)

        data = response.read()

        response.close()

        cache[URL] = data

        return cache[URL]

web_client('https://www.google.com')
web_client('https://www.google.com')

# what if the web page changes? data in cache would be stale!
# Won't cache grow without end?