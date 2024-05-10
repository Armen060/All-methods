# Ex_1 list
class MyList:
    def __init__(self, lst):
        self.lst = lst

    def append(self, item):
        self.lst.append(item)

    def extend(self, other_lst):
        self.lst.extend(other_lst)

    def insert(self, index, item):
        self.lst.insert(index, item)

    def remove(self, item):
        self.lst.remove(item)

    def pop(self, index=None):
        return self.lst.pop(index)

    def clear(self):
        self.lst.clear()

    def index(self, item):
        return self.lst.index(item)

    def count(self, item):
        return self.lst.count(item)

    def sort(self, reverse=False):
        self.lst.sort(reverse=reverse)

    def reverse(self):
        self.lst.reverse()

    def copy(self):
        return self.lst.copy()


# Ex_2 Tuple
class MyTuple:
    def __init__(self, tpl):
        self.tpl = tpl

    def __getitem__(self, index):
        return self.tpl[index]

    def __len__(self):
        return len(self.tpl)

    def __contains__(self, item):
        return item in self.tpl

    def count(self, item):
        return self.tpl.count(item)

    def index(self, item):
        return self.tpl.index(item)

#Ex_3 dictionary
class MyDict:
    def __init__(self, dct):
        self.dct = dct

    def __getitem__(self, key):
        return self.dct[key]

    def __setitem__(self, key, value):
        self.dct[key] = value

    def __delitem__(self, key):
        del self.dct[key]

    def __len__(self):
        return len(self.dct)

    def __contains__(self, key):
        return key in self.dct

    def keys(self):
        return self.dct.keys()

    def values(self):
        return self.dct.values()

    def items(self):
        return self.dct.items()

    def get(self, key, default=None):
        return self.dct.get(key, default)

    def clear(self):
        self.dct.clear()

    def update(self, other_dct):
        self.dct.update(other_dct)

    def copy(self):
        return self.dct.copy()

#Ex_4 Set

class MySet:
    def __init__(self, st):
        self.st = set(st)

    def add(self, elem):
        self.st.add(elem)

    def remove(self, elem):
        self.st.remove(elem)

    def discard(self, elem):
        self.st.discard(elem)

    def pop(self):
        return self.st.pop()

    def clear(self):
        self.st.clear()

    def copy(self):
        return self.st.copy()

    def union(self, other_set):
        return self.st.union(other_set)

    def intersection(self, other_set):
        return self.st.intersection(other_set)

    def difference(self, other_set):
        return self.st.difference(other_set)

    def symmetric_difference(self, other_set):
        return self.st.symmetric_difference(other_set)

    def issubset(self, other_set):
        return self.st.issubset(other_set)

    def issuperset(self, other_set):
        return self.st.issuperset(other_set)

    def isdisjoint(self, other_set):
        return self.st.isdisjoint(other_set)

    def __len__(self):
        return len(self.st)

    def __contains__(self, elem):
        return elem in self.st

    def __iter__(self):
        return iter(self.st)
