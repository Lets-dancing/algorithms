def big_num(n_count, nums):
    for i in range(n_count - 1):
        for j in range(0, n_count-i-1):
            var1 = nums[j] + nums[j+1]
            var2 = nums[j + 1] + nums[j]
            if var1 < var2:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(''.join(nums))


n_count = int(input())
nums = input().split(' ')
big_num(n_count, nums)
