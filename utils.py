#is brute force O(e)
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