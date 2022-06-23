def velo_prices(daysum, price, left, right):
    if left != 0 and right <= left:
        return -1
    mid = (left + right) // 2
    if daysum[mid] >= price and (daysum[mid - 1] < price or mid == 0):
        return mid + 1
    elif price <= daysum[mid]:
        return velo_prices(daysum, price, left, mid)
    else:
        return velo_prices(daysum, price, mid + 1, right)


days = int(input())
daysum = [int(num) for num in input().split(' ')]
price = int(input())

print(velo_prices(daysum, price, left=0, right=len(daysum)), end=' ')
print(velo_prices(daysum, price * 2, left=0, right=len(daysum)), end=' ')
