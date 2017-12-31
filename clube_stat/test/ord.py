
import collections

class Tables(collections.MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, item, value):
        self.data[item] = value

    def __delitem__(self, item):
        del(self.data[item])

    def __iter__(self):
        for x in self.data:
            yield x

    def __len__(self):
        return len(self.data)

od = Tables()

od["a"] = 1
od["b"] = 2

for k, i in od.items():
    print(k, i)


