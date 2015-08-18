__author__ = 'Henry Pan'


# Finding commonalities in Two Dictionaries

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# print a.keys() & b.keys()
# Unsupported operand type(s) for &
# print a.keys() - b.keys()
# print a.items() & b.items()


# Removing Duplicates from a Sequence while Maintaining Order

def deduplicate(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 1, 3, 4, 6, 10, 4, 9, 8, 4]
print list(deduplicate(a))


# If you want to eliminate duplicates in a sequence of un-hashable type(such a dictionary):

def deduplicate2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# if all you want do is eliminate duplicates, it is easy enough to make a set:
print set(a)  # this approach doesn't preserve any kind of ordering


