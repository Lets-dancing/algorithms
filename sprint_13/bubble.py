def bubble_sort(massive):
    for i in range(1, len(massive)):
        if massive[i] < massive[i - 1]:
            massive[i], massive[i - 1] = massive[i - 1], massive[i]


def check_sort(massive):
    for i in range(1, len(massive)):
        if massive[i] < massive[i - 1]:
            return False
    return True


n = int(input())
massive = [int(i) for i in input().split(' ')]
if check_sort(massive):
    print(*massive)
else:
    while not check_sort(massive):
        bubble_sort(massive)
        print(*massive)
