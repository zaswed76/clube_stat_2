import numpy as np

# x = [3, 5]
# y = [10, 14]
# yn = np.interp(7, x, y)
# print(yn)

x = [1, 2, 3, 4,  7, 8, 9]
y = [10 ,12, 20, 24, 12, 10, 7]

print(np.interp(5, x, y))
print(np.interp(6, x, y))


# def f1(lst):
#     h = []
#     m = []
#     for n, e in enumerate(lst):
#         if e is None:
#             last = n-1
#             next = n+1
#             h.append(last)
#             m.append(lst[last])
#             h.append(next)
#             m.append(lst[next])
#             return h, m
#
# print(f1(m))


