def flower_loc(garden_count, gardener):
    for i in range(garden_count):
        start, end = map(int, input().split())
        gardener[i] = [start, end]

    gardener.sort()
    results = []
    flowerbad = 0
    un_start, un_end = gardener[flowerbad]
    flowerbad += 1
    while flowerbad < garden_count:
        if un_start <= gardener[flowerbad][0] <= un_end:
            _, curr_end = gardener[flowerbad]
            flowerbad += 1
            if curr_end > un_end:
                un_end = curr_end
        else:
            results.append([un_start, un_end])
            un_start, un_end = gardener[flowerbad]
            flowerbad += 1
    results.append([un_start, un_end])

    for locs in results:
        print(*locs)


garden_count = int(input())
gardener = [None] * garden_count
flower_loc(garden_count, gardener)
