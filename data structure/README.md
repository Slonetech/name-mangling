list.append(x)

Adds an item to the end of the list.
Equivalent to a[len(a):] = [x].
python
Copy code
fruits = ['orange', 'apple', 'pear']
fruits.append('banana')
print(fruits)  # Output: ['orange', 'apple', 'pear', 'banana']
list.extend(iterable)

Extends the list by appending all items from the iterable.
Equivalent to a[len(a):] = iterable.
python
Copy code
fruits = ['orange', 'apple', 'pear']
fruits.extend(['banana', 'kiwi'])
print(fruits)  # Output: ['orange', 'apple', 'pear', 'banana', 'kiwi']
list.insert(i, x)

Inserts an item at a given position.
Example: a.insert(0, x) inserts at the front, a.insert(len(a), x) is equivalent to a.append(x).
python
Copy code
fruits = ['orange', 'apple', 'pear']
fruits.insert(1, 'banana')
print(fruits)  # Output: ['orange', 'banana', 'apple', 'pear']
list.remove(x)

Removes the first item from the list whose value is equal to x.
Raises a ValueError if there is no such item.
python
Copy code
fruits = ['orange', 'apple', 'pear']
fruits.remove('apple')
print(fruits)  # Output: ['orange', 'pear']
list.pop([i])

Removes and returns the item at the given position.
If no index is specified, removes and returns the last item.
python
Copy code
fruits = ['orange', 'apple', 'pear']
popped_item = fruits.pop(1)
print(popped_item)  # Output: 'apple'
print(fruits)       # Output: ['orange', 'pear']
list.clear()

Removes all items from the list.
Equivalent to del a[:].
python
Copy code
fruits = ['orange', 'apple', 'pear']
fruits.clear()
print(fruits)  # Output: []
list.index(x[, start[, end]])

Returns the index of the first item equal to x within optional start and end arguments.
Raises a ValueError if there is no such item.
python
Copy code
fruits = ['orange', 'apple', 'pear']
index = fruits.index('apple')
print(index)  # Output: 1
list.count(x)

Returns the number of times x appears in the list.
python
Copy code
fruits = ['orange', 'apple', 'pear', 'apple']
count = fruits.count('apple')
print(count)  # Output: 2
list.sort(*, key=None, reverse=False)

Sorts the items of the list in place with optional key and reverse arguments.
python
Copy code
fruits = ['orange', 'apple', 'pear']
fruits.sort()
print(fruits)  # Output: ['apple', 'orange', 'pear']
list.reverse()

Reverses the elements of the list in place.
python
Copy code
fruits = ['orange', 'apple', 'pear']
fruits.reverse()
print(fruits)  # Output: ['pear', 'apple', 'orange']
list.copy()

Returns a shallow copy of the list.
Equivalent to a[:].
python
Copy code
fruits = ['orange', 'apple', 'pear']
copy_of_fruits = fruits.copy()
print(copy_of_fruits)  # Output: ['orange', 'apple', 'pear']