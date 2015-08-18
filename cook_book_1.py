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


# Naming a slice
record = '....................100          .......513.25     ..........'
SHARES = slice(20, 32)
PRICE = slice(40, 48)

print int(record[SHARES]) * float(record[PRICE])

a = slice(10, 50, 2)
print a.start, a.stop, a.step

s = 'HelloWorld'
print a.indices(len(s))
for i in range(*a.indices(len(s))):
    print i
    print(s[i])

# Determine the Most Frequently Occurring Items in a Sequence
words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
print word_counts['under']


# Sorting a List of Dictionaries by a Common Key
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print rows_by_fname
print rows_by_uid

