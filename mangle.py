
# Mapping Class Definition
class Mapping:
    def __init__(self, iterable):
        # Initializing an empty list for items
        self.items_list = []
        # Using name mangling to call a private method during initialization
        self.__update(iterable)

    # Public update method to append items to the items_list
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    # Creating a private copy of the original update() method using name mangling
    __update = update

# MappingSubclass Inherits from Mapping
class MappingSubclass(Mapping):
    # Overriding the update method to provide a new signature without breaking the base class
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)

# Creating an instance of MappingSubclass
subclass_instance = MappingSubclass(['a', 'b'])

# Accessing and Printing the items_list, which is not private
print(subclass_instance.items_list)  # Output: ['a', 'b']

# Accessing the private method using name mangling to update items_list
subclass_instance._Mapping__update(['c', 'd'])

# Accessing and Printing the items_list again
print(subclass_instance.items_list)  # Output: ['a', 'b', 'c', 'd']
