arr = [1, 2, 4, 6, 8, 25]
target = 8

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print(f"Որոնվող արժեքը՝ {target}, գտնվել է ինդեքսում՝ {mid}")
        break
    elif arr[mid] > target:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("Արժեքը չի գտնվել")
