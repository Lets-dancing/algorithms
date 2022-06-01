# номер успешной посылки ID 68704642

def near_null(lenght, empty):
    lenght = len(fields)
    result = [0] * lenght
    empty = [field for field, value in enumerate(fields) if value == '0']
    for field in range(empty[0]):
        result[field] = empty[0] - field
    for index, _ in enumerate(empty):
        for field in range(empty[index - 1] + 1, empty[index]):
            result[field] = min(field - empty[index - 1], empty[index] - field)
    for field in range(empty[-1] + 1, lenght):
        result[field] = field - empty[-1]
    return result


if __name__ == '__main__':
    lenght = int(input())
    fields = input().split()
    empty = []
    res = near_null(lenght, empty)
    print(*res)
