class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.size = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        hash = 5381
        for i in key:
            hash = (hash << 5) + ord(i)
        return hash & 0xffffffff

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
        index = self.hash_index(key)
        cur = self.storage[index]
        if cur is None:
            self.storage[index] = HashTableEntry(key, value)
            self.size += 1
            return
        if cur.key == key:
            cur.value = value
            return
        while cur.next is not None:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        cur = self.storage[self.hash_index(key)]
        while cur.key is not key:
            if cur.next is None:
                return False
            cur = cur.next
        cur_val = None
        if cur.key is key:
            cur_val = cur.value
            cur.value = None
            self.size -= 1
        return cur_val

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        cur = self.storage[index]

        if cur is None:
            return False
        while cur.key is not key:
            if cur.next is None:
                return False
            cur = cur.next
        return cur.value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        prev_storage = self.storage
        if len(self.storage) // self.size > 0.7:
            print(".7 has been reached. Expanding...")
            self.capacity *= 2
            self.storage = [None] * self.capacity
            for i in prev_storage:
                while i is not None:
                    prev = i
                    i = prev.next
                    prev.next = None
                    self.put(prev.key, prev.value)

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")