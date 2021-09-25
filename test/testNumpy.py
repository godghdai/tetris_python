nums = [12, 20, 70, 22, 90]
total = sum(nums)
result = {num: round(num / total * 100, 2) for num in nums}
print(result[70])

import os

path = r"E:\新下载"

# for root, dirs, files in os.walk(path, topdown=True):
#     for name in dirs:
#         print(os.path.join(root, name))
#     for name in files:
#         print(os.path.join(root, name))


import glob

for name in glob.glob(R'E:\新下载\**', recursive=True):
    print(name)

dic = {
    "a": 4,
    "b": 2,
    "c": 1,
    "d": 2,
    "e": 3
}
result = {t[0]: t[1] for t in sorted(dic.items(), key=lambda t: t[1])}
print(result)

import collections

dic = collections.OrderedDict()
