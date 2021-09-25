import time


def insert(word, pos, char):
    if pos == 0:
        return char + word
    elif pos == len(word):
        return word + char
    return word[:pos] + char + word[pos:]


def result(word, letters):
    start, end = 0, len(letters)
    max_pos, pos = len(word), 0
    while start < end:
        if pos > max_pos:
            pos = 0
        else:
            yield insert(word, pos, letters[start])
            pos += 1
            continue
        start += 1


word = "A"
start = time.clock()
for n in result(word, [chr(ord('b') + c) for c in range(2)]):
    print(n)
elapsed = (time.clock() - start)
print("Time used:", elapsed)

start = time.clock()
for i in range(ord('b'), ord('b')+24):
    new = None
    for j in range(len(word)):
        if j == 0:
            new = chr(i) + word
            print(new)
        elif j == len(word)-1:
            new = word + chr(i)
            print(new)
        else:
            new = word[0:j] + chr(i) + word[j:]
            print(new)
elapsed = (time.clock() - start)
print("Time used:", elapsed)
