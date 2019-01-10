import gc


counter = 0

class SingleThreadObject(object):
    def __init__(self):
        global counter
        mark = counter
        a = list()
        for _ in range(10):
            a = [a]
            a.append(a)

        del a
        counter = mark + 1

    def __del__(self):
        global counter
        mark = counter
        counter = mark - 1


for _ in range(10000):
    a = list()
    b = list()
    a.append(b)
    b.append(a)
    a.append(SingleThreadObject())
    del a
    del b
    gc.collect() # if not como,mments, large number will shows up

# gc.collect()
print(counter)