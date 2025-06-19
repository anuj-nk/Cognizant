# Task 1
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("Original list:", fruits)

fruits.append('fig')
print("After adding a fruit:", fruits)

fruits.remove('apple')
print("After removing a fruit:", fruits)

reversed_fruits = fruits[::-1]
print("Reversed list:", reversed_fruits)

# Task 2
me = {
    "name": "Alice",
    "age": 25,
    "city": "Seattle"
}

me["favorite color"] = "Blue"

me["city"] = "New York"

print("Keys:", ", ".join(me.keys()))
print("Values:", ", ".join(str(v) for v in me.values()))

# Task 3
favorite_things = ('Inception', 'Bohemian Rhapsody', '1984')
print("Favorite things:", favorite_things)

try:
    favorite_things[0] = 'Interstellar'
except TypeError:
    print("Oops! Tuples cannot be changed.")

print("Length of tuple:", len(favorite_things))