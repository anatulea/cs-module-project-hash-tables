'''
- hash function + array = hash table
                 - array full of linked lists
Quick demo of handling a collision with a LL
Index     Chain
0          None
1          ('foo', 12)  --> ('bar', 42) --> ('xyzzy', 99)
2          None
3          ('baz', 13)
4          None
5          None
'''
put('foo', 12) # hash to 1
put('baz', 13)  # hash to 3
put('bar', 23) # hash to 1
put('bar', 42) # overwrite the 23
put('xyzzy', 99) # hashes to 1 as well!
get('bar')
'''
How do we do a get??
  How do we determine if it's the value we want if we're searching by the key?
  A: store the key unhashed, and compare as we iterate/traverse down the linked list
Put?
  Check if key is in linked list, if so overwite, if not add new Node
Delete?
delete('bar')
    - find the matching pair of values 
    - point the previous node of that one to the next node of the found node
Linked Lists
- Singly linked, node.next
- Doubly linked, node.next and node.prev
Node(next: 23_node, value: 12 ) ---> Node(next: None, value: 23)
'''
class SLL:
    def __init__(self):
        self.head = None
    def get(self, target_value):
        # start at the head
        node = self.head
        while node is not None:
        # check for the target value
            if node.value == target_value:
                return node
        # move to next node
            else:
                node = node.next
    def delete(self, target_value):
        # if it's head
        # if LL is empty
        if not self.head:
            return False
        if self.head.value == target_value:
            self.head = self.head.next
        prev_node = self.head
        cur_node = self.head.next
        while cur_node is not None:
            if cur_node.value == target_value:
                prev_node.next = cur_node.next
            else:
                prev_node = cur_node
                cur_node = cur_node.next
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

'''
LOAD FACTOR AND RESIZING
O(1)
0  -> A
1  -> B
2  -> C
3  -> D -> F
4  -> E
5
O(N)
0  -> A 
1  -> B --> G --> L --> M
2  -> C --> K
3  -> D --> H
4  -> E --> J
5  -> F --> I
load factor
(number of elements) / (number of slots)
1.0
> 2
Load factor < 0.7
If load factor < 0.2, hash table is underloaded, so array is bigger than you need
How to resize?
- How do we resize arrays?
-- make a new array, double the size of the old one
-- iterate down the old array, and copy every item over
-- so it's O(n)
- For a hash table:
-- double your backing array
-- iterate down the old array
--- and traverse down the linked list
--- then do a put (aka: hash the key, mod key, put into a node)
Checklist
- Go down checklist
- What took me the longest?
- run, right, fast
- binary search to debug
- Could I find what I was looking for?
Vimium plugin
games to play vim
- keyboard macros
BTW I have no special Vim plugins, I just jump around using standard Vim.
And I could be faster, I forget to use paragraph jumps and so on.
'''