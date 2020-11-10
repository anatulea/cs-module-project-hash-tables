class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

MAX_LOAD_FACTOR = 0.7   
MIN_LOAD_FACTOR = 0.2

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        if capacity >= MIN_CAPACITY:
            self.capacity = max(capacity, MIN_CAPACITY)
            self.mylist = [None] * capacity
            self.load = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        return self.load / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211

        hashed = FNV_offset_basis

        bytes_to_hash = key.encode()

        for byte in bytes_to_hash:
            hashed = hashed * FNV_prime
            hashed = hashed ^ byte # 	XOR	Sets each bit to 1 if only one of two bits is 1
            return hashed


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        hash = 5381
        for character in key:
            hash = ((hash << 5)+hash)+ord(character)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)
        entry = self.mylist[slot]

        # if there is no slot present
        if entry is None:
            # create a new hash tabe entry and add it to that slot
            self.mylist[slot] = HashTableEntry(key, value)
            # increase the load by one
            self.load += 1
            # check if resizeing is needed
            self.resizeIfNeeded()
            return

        #while the slot has a next value is present and thee slot key isn not equal to the key we want to add
        while entry.next != None and entry.key !=key:
            # we set the current entry to be equal to the nexo slot
            entry = entry.next
        # if the slot key is equal to the one we want to insert
        if entry.key == key:
            # we set the value of it to the vakue we want to insert
            entry.value = value
        else:# else if slot key is not equal to our key 
            # set the next value of the slot to a new hash table entry
            entry.next = HashTableEntry(key, value)
            self.load += 1
            self.resizeIfNeeded()


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        slot = self.hash_index(key)
        entry = self.mylist[slot]
        prev_entry = None

        if entry is not None:
            while entry.next != None and entry.key != key:
                prev_entry = entry
                entry = entry.next

            if entry.key == key:
                if prev_entry is None:
                    self.mylist[slot] = entry.next
                else: 
                    prev_entry.next = entry.next
                    self.load -= 1
                    self.resizeIfNeeded()
                return


    def get(self, key):

        slot = self.hash_index(key)
        entry = self.mylist[slot]

        if entry is None:
            return None
        
        while entry.next != None and entry.key != key:
            entry = entry.next

        return entry.value if entry.key == key else None


    def resizeIfNeeded(self):
         if self.get_load_factor () > MAX_LOAD_FACTOR:
                self.resize(self.capacity * 2)
         elif self.get_load_factor() < MIN_LOAD_FACTOR and int(self.capacity / 2) >= MIN_CAPACITY:
            self.resize(int(self.capacity / 2))

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """

        old_mylist = self.mylist
        self.mylist = [None] * new_capacity
        self.capacity = new_capacity

        for old_entry in old_mylist:
            while old_entry is not None:
                key = old_entry.key
                value = old_entry.value
                index = self.hash_index(key)
                entry = self.mylist[index]
                
                if entry is None:
                    self.mylist[index] = HashTableEntry(key, value)
                else: 
                    while entry.next != None:
                        entry = entry.next
                    entry.next = HashTableEntry(key, value)

                old_entry = old_entry.next
      


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")