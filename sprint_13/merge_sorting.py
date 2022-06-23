def merge(arr, lf, mid, rg):
    result = list()
    half_1 = arr[lf: mid]
    half_2 = arr[mid: rg]
    if not half_1:
        return half_2
    if not half_2:
        return half_1
    index_1 = 0
    index_2 = 0
    result = []
    while True:
        value_1 = half_1[index_1]
        value_2 = half_2[index_2]
        if value_1 < value_2:
            result += [value_1]
            index_1 += 1
        else:
            result += [value_2]
            index_2 += 1
        if index_1 == len(half_1):
            ended = 1
            break
        if index_2 == len(half_2):
            ended = 2
            break
    if ended == 2:
        while index_1 < len(half_1):
            result += [half_1[index_1]]
            index_1 += 1
    else:
        while index_2 < len(half_2):
            result += [half_2[index_2]]
            index_2 += 1
    return result


def merge_sort(arr, lf, rg):
    if rg - lf <= 1:
        return
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    arr[lf: rg] = merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
