# 58_kadanes_and_subarray_algorithms.py
# Kadane's Algorithm & Subarray Algorithms - 10 practical programs/features

def kadane(arr):
    best = current = arr[0]
    for x in arr[1:]:
        current = max(x, current + x)
        best = max(best, current)
    return best

def max_subarray_with_indices(arr):
    best = current = arr[0]
    best_l = best_r = current_l = 0
    for i in range(1, len(arr)):
        if arr[i] > current + arr[i]:
            current = arr[i]
            current_l = i
        else:
            current += arr[i]
        if current > best:
            best = current
            best_l, best_r = current_l, i
    return best, best_l, best_r

def min_subarray_sum(arr):
    current = best = arr[0]
    for x in arr[1:]:
        current = min(x, current + x)
        best = min(best, current)
    return best

def max_circular_subarray(arr):
    normal = kadane(arr)
    total = sum(arr)
    inverted = kadane([-x for x in arr])
    circular = total + inverted
    return normal if circular == 0 else max(normal, circular)

def longest_positive_sum_subarray(arr):
    best_len = best_l = best_r = 0
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            if total > 0 and j - i + 1 > best_len:
                best_len, best_l, best_r = j - i + 1, i, j
    return arr[best_l:best_r + 1]

def count_subarrays_with_sum(arr, target):
    counts = {0: 1}
    prefix = answer = 0
    for x in arr:
        prefix += x
        answer += counts.get(prefix - target, 0)
        counts[prefix] = counts.get(prefix, 0) + 1
    return answer

def max_product_subarray(arr):
    best = hi = lo = arr[0]
    for x in arr[1:]:
        if x < 0:
            hi, lo = lo, hi
        hi = max(x, hi * x)
        lo = min(x, lo * x)
        best = max(best, hi)
    return best

# 1. Basic Kadane
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("1. Maximum subarray sum:", kadane(a))

# 2. Return subarray indices
print("2. Best sum and indices:", max_subarray_with_indices(a))

# 3. Extract maximum-sum subarray
_, left, right = max_subarray_with_indices(a)
print("3. Maximum-sum subarray:", a[left:right + 1])

# 4. Minimum subarray sum
print("4. Minimum subarray sum:", min_subarray_sum(a))

# 5. Maximum circular subarray
print("5. Maximum circular subarray sum:", max_circular_subarray([5, -3, 5]))

# 6. Longest subarray with positive sum (educational O(n^2) version)
print("6. Longest positive-sum subarray:", longest_positive_sum_subarray([-1, 2, 3, -5, 4, 2]))

# 7. Count subarrays having a target sum
print("7. Count sum=3:", count_subarrays_with_sum([1, 2, 1, 1, 1], 3))

# 8. Maximum product subarray
print("8. Maximum product:", max_product_subarray([2, 3, -2, 4]))

# 9. All-positive special case
print("9. All-positive array:", kadane([1, 2, 3, 4]))

# 10. All-negative special case
print("10. All-negative array:", kadane([-8, -3, -6, -2, -5, -4]))
