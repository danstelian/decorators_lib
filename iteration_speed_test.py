# from decorators_lib import decolib
import decolib


reps = list(range(10000))


@decolib.timeit(1000)
def forloop():
    res = []
    for x in reps:
        res.append(x * x)
    return res


@decolib.timeit(1000)
def listcomp():
    return [x * x for x in reps]


@decolib.timeit(1000)
def mapcall():
    return list(map(lambda x: x * x, reps))


@decolib.timeit(1000)
def genexpr():
    return list(x * x for x in reps)


@decolib.timeit(1000)
def genfunc():
    def gen():
        for x in reps:
            yield x * x
    return list(gen())


print(forloop()[0])
print(listcomp()[0])
print(mapcall()[0])
print(genexpr()[0])
print(genfunc()[0])
