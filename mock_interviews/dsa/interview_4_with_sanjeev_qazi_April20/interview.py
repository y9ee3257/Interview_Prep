'''
/*
 Write an implementation of the following interface for a key value store:

   void   put(key, val);
   V        get(key);
   void  delete(key);
   K       last();             // returns the last-accessed (put or get), non-deleted key
   K       random();    // returns a random key
 }

Example:
   put("a", 1)
   last()                      => "a"
   last()                      => "a"

   put("b", 2)
   last()                      => "b"

   get("a")                 => 1
   last()                      => "a"

   delete("a")
   last()                      => "b"

   get a
   get b
   get c
      get a
   delete c

 delete - ()


   a
   b
   c
   d
   e
   g
   f

    c
    b
    a


    a  <-> c  <-> b

    {
        a : linkedlist, index
        b : linkedlist, index
        c : linkedlist, index
    }



    [a, d, c, b]


    O(n) space

    put
    get
    last O(1)

'''
import math


class LinkedList:

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next




class KeyValueStore:


    def __init__(self):
        self.map = {}
        self.arr = []
        self.tail = None



    def get(self, key):
        if key in self.map:
            curr_ll, _ = self.map[key]
            prev = curr_ll.prev # a -> c -> b
            if prev:
                prev.next = curr_ll.next

            # update current linked list to tail
            curr_ll.prev = self.tail
            curr_ll.next = None
            self.tail = curr_ll
            return curr_ll.value
        return None


    def put(self, key, value):
        if key in self.map:
            curr_ll, _ = self.map[key]
            curr_ll.value = value
            self.get(key)
        else:
            self.arr.append(key)
            ll = LinkedList(value, self.tail, None)
            self.map[key] = (ll, len(self.arr)-1)  # { a : (ll, 2) }


    def last(self):

        if self.tail:
            return self.tail.value

        return None


    def random(self):
        rand_index = math.random(0,len(self.arr)-1)
        return self.arr[rand_index]


    def remove(self, key):
        if key in self.map:
            curr_ll, arr_index = self.map[key]
            prev = curr_ll.prev

            if prev:
                prev.next = curr_ll.next

            del self.map[key]

            last_key = self.arr[-1]
            self.map[last_key] = (self.map[last_key][0], arr_index)

            self.arr[arr_index], self.arr[-1] = self.arr[-1], self.arr[arr_index]

            self.arr.pop()



























































