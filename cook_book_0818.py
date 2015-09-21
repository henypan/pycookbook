__author__ = 'Henry Pan'


# Sorting Objects without Native Comparison Support
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(100), User(12), User(50)]

print sorted(users, key=lambda u: u.user_id)

from operator import attrgetter
print sorted(users, key=attrgetter('user_id'))


# Grouping based on a Field
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))  # need to sort the rows data first, then call groupby

for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for item in items:
        print '  ', item


# Filtering Sequence Elements

mylist = [10, 3, -2, -8, 99, 21, -90, -5, 18]
res = [n for n in mylist if n > 0]
print res

# Or use the generator if list comprehension is large
res2 = (n for n in mylist if n > 0)
for r in res2:
    print r

for r in res2:
    print r # no value printed

# Or use built-in function filter()
mylist = [10, 3, -2, -8, 99, 'N/A', 21, -90, -5, 18]


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, mylist))
print ivals


def gte_zero(val):
    if is_int(val):
        if int(val) > 0:
            return True
        else:
            return False
    else:
        return False

evals = list(filter(gte_zero, mylist))
print evals


# Compress
addresses = [
    '5412 N CLARK',  # 0
    '5148 N CLARK',  # 3
    '5800 E 58TH',   # 10
    '2122 N CLARK'   # 4
    '5645 N RAVENSWOOD',  # 1
    '1060 W ADDISON',  # 7
    '4801 N BROADWAY',  # 6
    '1039 W GRANVILLE',  # 1
]

counts = [6, 3, 10, 4, 1, 6, 2, 4]
from itertools import compress
more5 = [n > 5 for n in counts]
print more5
print list(compress(addresses, more5))   # TODO - result seems to be wrong


# Extracting a Subset of a Dictionary
prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

p1 = {key: value for key, value in prices.items() if value > 100}
print p1

# Mapping Names to Sequence Elements
