"""
Homegrown decorators lib
@timeit - timing decorator
"""
import time
from functools import wraps


timer = time.perf_counter


def timeit(reps=1):

    def decorateit(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            # total time for number of reps
            t0 = timer()
            for i in range(reps):
                result = func(*args, **kwargs)
            total_time = timer() - t0

            # best time
            best_time = 2 ** 32
            for i in range(reps):
                t0 = timer()
                result = func(*args, **kwargs)
                elapsed = timer() - t0
                if elapsed < best_time:
                    best_time = elapsed

            name = func.__name__
            ret_str = f'{name}: BEST:[{best_time:.8f}s] * {reps} -> TOTAL:[{total_time:.8f}s]'
            return ret_str, result

        return wrapper

    return decorateit


def clock(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = timer()
        result = func(*args, **kwargs)
        elapsed = timer() - t0

        name = func.__name__
        ret_str = f'{name}: TIME:[{elapsed:.8f}s] -> RESULT:[{result}]'
        print(ret_str)

        return result

    return wrapper
