#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size

    def cobble(self):
        print(f"Your shoe is as good as new!")

    def condition(self):
        return "New"

    def set_size(self, size):
        if (type(size) is not int):
            print("size must be an integer")
        else:
            self._size = size

    def get_size(self):
        return self._size
    
    size = property(get_size, set_size)