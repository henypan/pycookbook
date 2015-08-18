__author__ = 'Henry Pan'


# Unpacking a sequence into Separate variables
data = ['ACME', 50, 90.1, (2015, 12, 10)]
_, shares, prices, (year, month, day) = data

print shares
print prices
print year, month, day


# Unpacking Elements from Iterables of Arbitrary Length
def unpack_three(name, email, *phone):
    return name, email, phone

record = ('Henry', 'henrypan917@gmail.com', '917-349-9877', '917-349-2966')
name, email, phone_numbers = unpack_three(*record)
print name, email, phone_numbers


# Keeping the last N Items
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for tline in lines:
        if pattern in tline:
            yield tline, previous_lines
            previous_lines.append(tline)

with open('code_book_0817_some_text.txt') as f:
    for line, prevlines in search(f, 'python', 5):
        for pline in prevlines:
            print pline
        # print line
        print '-'*20


# What is yield in Python?
import webbrowser
# webbrowser.open_new('http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python')


# Find the Largest or Smallest of N Items
import heapq
print heapq.nsmallest(4, [12, 323, 12, 89, 2, -1, 290])
print heapq.nlargest(4, [12, 323, 12, 89, 2, -1, 290])

stocks = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YAHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap_stock = heapq.nsmallest(3, stocks, key=lambda s: s['price'])
expensive_stock = heapq.nlargest(3, stocks, key=lambda s: s['price'])
print 'Top 3 cheap stocks:', [stock['name'] for stock in cheap_stock]
print 'Top 3 expensive stocks:', [stock['name'] for stock in expensive_stock]


# Mapping Keys to Multiple Values in a Dictionary
# Use default dictionary
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)

print d

pairs = [
    ['a', [1, 2, 3]],
    ['b', [4, 5]],
    ['c', [8, 9]]
]

c = defaultdict(list)
for key, value in pairs:
    c[key].extend(value)

print c


# Keeping Dictionaries in Order
from collections import OrderedDict

d = OrderedDict()
d['a'] = 'apple'
d['b'] = 'banana'
d['c'] = 'carrot'
d['d'] = 'dog'

for key in d:
    # print out in order
    print d[key]
print('OrderedDict is more than the twice as large as a normal dictionary')


# Calculating with Dictionary
prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

sorted_prices = sorted(zip(prices.values(), prices.keys()))
print 'Sorted by prices: ', sorted_prices
print 'Min price: ', min(prices)
print 'Max price: ', max(prices)
print 'Sorted by prices(key): ', sorted(prices)


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

