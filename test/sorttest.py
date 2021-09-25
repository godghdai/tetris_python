def pick(iterable, fun):
    res = list()
    for num in iterable:
        res.append(fun(num))
    return res


arr = [("a", 1), ("b", 2), ("c", 3)]
print(pick(arr, lambda x: x[0]))

