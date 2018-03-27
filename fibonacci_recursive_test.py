import decolib
from functools import lru_cache


@decolib.clock
def recursive_fibonacci(n):
    return n if n < 2 else recursive_fibonacci(n - 2) + recursive_fibonacci(n - 1)


# recursive_fibonacci(7)


# result without the lru_cache() decorator:

# recursive_fibonacci: TIME:[0.00000075s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00000061s] -> RESULT:[0]
# recursive_fibonacci: TIME:[0.00000089s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00002974s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00008739s] -> RESULT:[2]
# recursive_fibonacci: TIME:[0.00000041s] -> RESULT:[0]
# recursive_fibonacci: TIME:[0.00000083s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00002391s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00000045s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00000066s] -> RESULT:[0]
# recursive_fibonacci: TIME:[0.00000081s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00002575s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00004922s] -> RESULT:[2]
# recursive_fibonacci: TIME:[0.00009594s] -> RESULT:[3]
# recursive_fibonacci: TIME:[0.00020622s] -> RESULT:[5]
# recursive_fibonacci: TIME:[0.00000038s] -> RESULT:[0]
# recursive_fibonacci: TIME:[0.00000080s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00002363s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00000042s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00000046s] -> RESULT:[0]
# recursive_fibonacci: TIME:[0.00000079s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00002398s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00004729s] -> RESULT:[2]
# recursive_fibonacci: TIME:[0.00009334s] -> RESULT:[3]
# recursive_fibonacci: TIME:[0.00000042s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00000047s] -> RESULT:[0]
# recursive_fibonacci: TIME:[0.00000080s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00002442s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00006714s] -> RESULT:[2]
# recursive_fibonacci: TIME:[0.00000045s] -> RESULT:[0]
# recursive_fibonacci: TIME:[0.00000083s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00002428s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00000044s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00000059s] -> RESULT:[0]
# recursive_fibonacci: TIME:[0.00000080s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00002510s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00004863s] -> RESULT:[2]
# recursive_fibonacci: TIME:[0.00009604s] -> RESULT:[3]
# recursive_fibonacci: TIME:[0.00018747s] -> RESULT:[5]
# recursive_fibonacci: TIME:[0.00030385s] -> RESULT:[8]
# recursive_fibonacci: TIME:[0.00053407s] -> RESULT:[13]


@lru_cache()
@decolib.clock
def recursive_fibonacci(n):
    return n if n < 2 else recursive_fibonacci(n - 2) + recursive_fibonacci(n - 1)


recursive_fibonacci(7)


# result with the lru_cache() decorator:

# recursive_fibonacci: TIME:[0.00000066s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00000074s] -> RESULT:[0]
# recursive_fibonacci: TIME:[0.00002015s] -> RESULT:[1]
# recursive_fibonacci: TIME:[0.00009200s] -> RESULT:[2]
# recursive_fibonacci: TIME:[0.00000142s] -> RESULT:[3]
# recursive_fibonacci: TIME:[0.00011771s] -> RESULT:[5]
# recursive_fibonacci: TIME:[0.00000128s] -> RESULT:[8]
# recursive_fibonacci: TIME:[0.00014479s] -> RESULT:[13]
