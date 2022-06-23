def wardrobe_sort(clo_count, array):
    colors = [0, 0, 0]
    colors[0] = array.count(0)
    colors[1] = array.count(1)
    colors[2] = array.count(2)
    index = 0
    for value in range(3):
        for _ in range(colors[value]):
            array[index] = value
            index += 1
    return array


clo_count = int(input())
massive = list(map(int, input().split()))
print(*wardrobe_sort(clo_count, massive))
