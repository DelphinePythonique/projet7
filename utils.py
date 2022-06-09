from itertools import count, cycle, repeat, accumulate, chain, compress, dropwhile, filterfalse, groupby, islice, \
    starmap, takewhile, tee, zip_longest, product, permutations, combinations
from time import perf_counter


def measure(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            end_ = perf_counter() - start
            print(f"{func.__name__}  execution time: {end_ if end_ >0 else 0} s")

    return wrapper


@measure
def test_count():
    for c in count(10):
        print(c)
        if c > 20:
            break


@measure
def test_cycle():
    nb_repeat = 0
    for c in cycle("ABCD"):
        print(c)
        nb_repeat += 1
        if nb_repeat > 15:
            break


@measure
def test_repeat():
    nb_repeat = 0
    for c in repeat("ABCD", 3):
        print(c)
        nb_repeat += 1
        if nb_repeat > 15:
            break


@measure
def test_accumulate():
    for c in accumulate([1, 2, 3, 4, 5]):
        print(c)


@measure
def test_chain():
    print("chain")
    for c in chain("ABC", "DEF"):
        print(c)
    print("chain iterable")
    for c in chain.from_iterable(["ABC", "DEF"]):
        print(c)


@measure
def test_compress():
    for c in compress("ABCDEF", [1, 0, 1, 0, 1, 1]):
        print(c)


@measure
def test_dropwhile():
    for c in dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]):
        print(c)

@measure
def test_filterfalse():
    for c in filterfalse(lambda x: x%2, range(10)):
        print(c)

@measure
def test_groupby():
   print([k for k, g in groupby('AAAABBBCCDAABBB')] )
   print([list(g) for k, g in groupby('AAAABBBCCDAABBB')])

   print([k for k, g in groupby('AAAABBBCCD')] )
   print([list(g) for k, g in groupby('AAAABBBCCD')] )

@measure
def test_islice():
    for c in islice('ABCDEFG', 2, None):
        print(c)
@measure
def test_starmap():
    for c in starmap(pow, [(2,5), (3,2), (10,3)]):
        print (c)

@measure
def test_takewhile():
    for c in takewhile(lambda x: x < 5, [1, 4, 6, 4, 1]):
        print(c)
@measure
def test_tee():
     # initializing list
    li = [2, 4, 6, 7, 8, 10, 20]

    # storing list in iterator
    iti = iter(li)

    # using tee() to make a list of iterators
    # makes list of 3 iterators having same values.
    #it = tee(iti, 3)
    it = tee(li, 3)


    # printing the values of iterators
    print ("The iterators are : ")
    for i in range (0, 3):
        print (list(it[i]))

@measure
def test_ziplongest():
    for c in zip_longest('ABCD', 'xy', fillvalue='-'):
        print(c)

@measure
def test_product():
    for c in product('ABCD', 'xy'):
        print(c)

    for c in product(range(2), repeat=2):
        print(c)

@measure
def test_permutation():
    for c in permutations('ABCD', 2):
        print(c)

    for c in  permutations(range(3)):
        print(c)

@measure
def test_combination():
    """
    for c in combinations('ABCD', 2) :
        print(c)
    """
    my_list = ["action1","action2","action3","action4"]
    for i in range(len(my_list)):
        result = combinations(my_list,r=i+1)
        for r in result:
            print(f"i:{i} - '{r}'")
@measure
def combination_index_list(n):
    list_n = []
    if n == 0:
        return [(0,)]
    else:
        list_minus_one = combination_index_list(n - 1)
        list_n.extend(list_minus_one)
        for combination in list_minus_one:
            combination_format_list = list(combination)
            combination_format_list.append(n)
            list_n.append(tuple(combination_format_list))
        list_n.append((n,))
        return list_n



test_combination()

result = combination_index_list(3)
for r in result:
    print(f"'{r}'")

"""
test_count()
test_cycle()
test_repeat()
test_accumulate()
test_chain()
test_compress()
test_dropwhile()
test_filterfalse()
test_groupby()
test_islice()
test_starmap()
test_takewhile()
test_tee()
test_ziplongest()
test_product()
test_permutation()
test_combination()
"""