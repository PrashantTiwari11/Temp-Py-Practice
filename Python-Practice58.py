"""51 - Interview Problem Solving: 10 practical programs"""

# 1. Two Sum
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen: return seen[target-n], i
        seen[n] = i
print("1.", two_sum([2,7,11,15], 9))

# 2. Majority element
def majority(nums):
    candidate, count = None, 0
    for n in nums:
        if count == 0: candidate = n
        count += 1 if n == candidate else -1
    return candidate
print("2.", majority([2,2,1,2,3,2,2]))

# 3. Missing number
def missing_number(nums):
    result = len(nums)
    for i, n in enumerate(nums): result ^= i ^ n
    return result
print("3.", missing_number([3,0,1]))

# 4. Move zeroes
def move_zeroes(nums):
    pos = 0
    for n in nums:
        if n: nums[pos], pos = n, pos + 1
    nums[pos:] = [0] * (len(nums)-pos)
    return nums
print("4.", move_zeroes([0,1,0,3,12]))

# 5. Best stock profit
def max_profit(prices):
    low, best = float("inf"), 0
    for p in prices:
        low = min(low, p); best = max(best, p-low)
    return best
print("5.", max_profit([7,1,5,3,6,4]))

# 6. Valid parentheses
def valid_parentheses(s):
    pairs, stack = {")":"(", "]":"[", "}":"{"}, []
    for ch in s:
        if ch in "([{": stack.append(ch)
        elif not stack or stack.pop() != pairs[ch]: return False
    return not stack
print("6.", valid_parentheses("{[()]}"))

# 7. Longest consecutive sequence
def longest_consecutive(nums):
    values, best = set(nums), 0
    for n in values:
        if n-1 not in values:
            length = 1
            while n+length in values: length += 1
            best = max(best, length)
    return best
print("7.", longest_consecutive([100,4,200,1,3,2]))

# 8. Product except self
def product_except_self(nums):
    result, prefix, suffix = [1]*len(nums), 1, 1
    for i,n in enumerate(nums): result[i], prefix = prefix, prefix*n
    for i in range(len(nums)-1,-1,-1):
        result[i] *= suffix; suffix *= nums[i]
    return result
print("8.", product_except_self([1,2,3,4]))

# 9. Rotate array
def rotate(nums, k):
    k %= len(nums); nums[:] = nums[-k:] + nums[:-k]
    return nums
print("9.", rotate([1,2,3,4,5], 2))

# 10. Merge intervals
def merge_intervals(intervals):
    intervals.sort(); merged = []
    for start,end in intervals:
        if not merged or start > merged[-1][1]: merged.append([start,end])
        else: merged[-1][1] = max(merged[-1][1], end)
    return merged
print("10.", merge_intervals([[1,3],[2,6],[8,10],[9,12]]))
