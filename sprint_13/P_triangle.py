def p_triangle(nums):
    nums.sort(reverse=True)
    for i in range(len(nums)):
        first = nums[i]
        for j in range(i + 1, len(nums) - 1):
            second = nums[j]
            for k in range(j + 1, len(nums)):
                two_sum = second + nums[k]
                if two_sum > first:
                    return two_sum + first


if __name__ == '__main__':
    _ = int(input())
    segments = list(map(int, input().split()))

    print(p_triangle(segments))
