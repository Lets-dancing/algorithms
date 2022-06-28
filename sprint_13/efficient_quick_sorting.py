# номер успешной посылки ID 69218253

def partition(arr, left, right):
    if right <= left:
        return
    left_index = left
    right_index = right
    pivot = (left + right) // 2
    reference = arr[pivot]
    while left_index <= right_index:
        while reference > arr[left_index]:
            left_index += 1
        while reference < arr[right_index]:
            right_index -= 1
        if left_index <= right_index:
            (arr[left_index],
             arr[right_index]) = (arr[right_index],
                                  arr[left_index])
            left_index += 1
            right_index -= 1
    partition(arr, left, right_index)
    partition(arr, left_index, right)


def quicksort(players):
    partition(players, 0, len(players) - 1)
    return [row[2] for row in players]


if __name__ == '__main__':
    clear_count = int(input())
    participant = []
    for _ in range(clear_count):
        name, clear, penalty = input().split()
        participant.append((-int(clear), int(penalty), name))
    result = quicksort(participant)
    print(*result, sep='\n')
