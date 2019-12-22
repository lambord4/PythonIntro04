from random import randint


def measure_time(arg):
    from datetime import datetime
    print(arg)

    def outer(function):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            res = function(*args, **kwargs)
            dt = datetime.now() - start
            print(dt)
            return res
        return wrapper
    return outer


@measure_time('GEN_1')
def gen_1(num):
    lst = []
    for _ in range(num):
        lst.append(randint(1, 100))

    return lst


@measure_time('GEN_2')
def gen_2(num):
    lst = [randint(1, 100) for _ in range(num)]

    return lst


print(len(gen_1(10**6)))
print(len(gen_2(10**6)))

f = measure_time

# print(f)
# print(f(gen_1)())
measure_time('GEN')(gen_1)(3)
