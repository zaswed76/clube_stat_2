from pandas import Series
from random import shuffle


d1 = dict(a=1,b=2, d=4, e=5)




obj1 = Series(d1)
obj2 = obj1.reindex(["a", "b", "c", "d", "e"], method="bfill")
print(obj2)





