# %% [markdown]
# # Collections

# %% [markdown]
# The `collections` module provides different types of containers.

# %%
import collections

dir(collections)

# %% [markdown]
# ## Counter

# %%
from collections import Counter


a_list = [1, 2, 2, 3, 4, 4, 4, 10]
a_string = "CodeFirstGirls"
a_dict = {"a": 5, "b": 3, "c": 5, "d": 5, "e": 1}

c_list = Counter(a_list)
c_string = Counter(a_string)
c_dict = Counter(a_dict.values())

print(c_list)
print(c_string)
print(c_dict)

c_list.update([2])
print(c_list)

# %% [markdown]
# ## OrderedDict
# Less important since Python 3.7, when the built-in `dict` class gained the ability to remember insertion order.

# %%
from collections import OrderedDict

d = OrderedDict([("apple", 5), ("orange", 6)])
print(d)

d["kiwi"] = 7
print(d)

d["melon"] = 8
print(d)

# create empty OrderedDict and populate

o = OrderedDict()
o["key1"] = "value1"
o["key2"] = "value2"
print(o)

# %% [markdown]
# ## DefaultDict
# Like `dict`, but never raises a `KeyError` - returns a default value instead.

# %%
from collections import defaultdict

state_capitals = defaultdict(str)
print(state_capitals)

state_capitals["Alaska"]
print(state_capitals)


# list example

basket = [("Fruit", "Pear"), ("Vegetable", "Tomato"), ("Fruit", "Peach")]
dd = defaultdict(list)

for k, v in basket:
    dd[k].append(v)

print(dd)

# %% [markdown]
# ## NamedTuple
# Quick way of grouping together some data - similar to classes. It's like a dictionary - contains labels and values, but unlike a dictionary, you can access values using a key as well as iteration. Immutable.

# %%
from collections import namedtuple


Person = namedtuple("Person", ["age", "height", "name"])

# alternatively

Person1 = namedtuple("Person", "age height name")

anna = Person(30, 165, "Anna")
marie_liz = Person1(age=25, height=178, name="Marie Elizabeth")

print(anna.age)
print(anna.name)
print(anna[1])


"""
The first argument to the namedtuple constructor (in our example 'Person') is the typename. 
It is typical to use the same word for the constructor and the typename, but they can be different:
"""

Human = namedtuple("Person", "age, height, name")
sophie = Human(40, 175, "Sophie")
print(sophie)

# %% [markdown]
# ## ChainMap

# %%

from collections import ChainMap

# define two dictionaries with at least some keys overlapping.
dict1 = {"apple": 1, "banana": 2}
dict2 = {"coconut": 1, "date": 1, "apple": 3}

# create two ChainMaps with different ordering of those dicts.
combined_dict = ChainMap(dict1, dict2)
reverse_ordered_dict = ChainMap(dict2, dict1)

print(combined_dict)

for k, v in combined_dict.items():
    print(k, v)


print(reverse_ordered_dict)

for k, v in reverse_ordered_dict.items():
    print(k, v)


# %% [markdown]
# ## Deque
# Doubled Ended Queue

# %%
from collections import deque

d = deque("CodeFirst")

for elem in d:
    print(elem.upper())

d.append("!")
d.appendleft("*")

print(d)

d.pop()
print(d)
d.popleft()
print(d)

d.extend("123")
print(d)

d.rotate(1)
print(d)

d.rotate(-1)
print(d)

d.clear()

# this will throw error as we cannot pop from empty deque
# d.pop()

d.extendleft("abc")
print(d)

# Can also speciy a maxlen

# %% [markdown]
# ## UserList, UserDict, UserString
# Wrapper around the original object (list, dict, string) to allow us to create our own list/dist/string with some modified or additional functionality.

# %%
from collections import UserList


class MyUniqueList(UserList):
    def add_in_middle(self, item):
        count = -1
        for i in self:
            count += 1

        self[int(count / 2)] = item


my_list = MyUniqueList([1, 2, 3, 4, 5])
print(my_list)

my_list.add_in_middle("CFG")
print(my_list)
