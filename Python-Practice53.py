# Day 12 - 46: Sliding Window & Two Pointers

# 1. Maximum sum of fixed-size window
a, k = [2, 1, 5, 1, 3, 2], 3
window = sum(a[:k])
best = window
for i in range(k, len(a)):
    window += a[i] - a[i-k]
    best = max(best, window)
print("1. Max window sum:", best)

# 2. Average of every window
a, k = [1, 3, 2, 6, -1, 4, 1, 8, 2], 5
window = sum(a[:k])
averages = [window / k]
for i in range(k, len(a)):
    window += a[i] - a[i-k]
    averages.append(window / k)
print("2. Averages:", averages)

# 3. Longest substring with at most 2 distinct characters
s = "eceba"
left = best = 0
counts = {}
for right, ch in enumerate(s):
    counts[ch] = counts.get(ch, 0) + 1
    while len(counts) > 2:
        counts[s[left]] -= 1
        if counts[s[left]] == 0:
            del counts[s[left]]
        left += 1
    best = max(best, right-left+1)
print("3. Longest length:", best)

# 4. Minimum subarray length with sum >= target
a, target = [2, 3, 1, 2, 4, 3], 7
left = total = 0
best = float("inf")
for right, x in enumerate(a):
    total += x
    while total >= target:
        best = min(best, right-left+1)
        total -= a[left]
        left += 1
print("4. Minimum length:", best)

# 5. Move zeroes to end
a = [0, 1, 0, 3, 12]
pos = 0
for x in a:
    if x != 0:
        a[pos] = x
        pos += 1
while pos < len(a):
    a[pos] = 0
    pos += 1
print("5. Move zeroes:", a)

# 6. Two Sum in sorted array
a, target = [1, 2, 4, 6, 8, 9], 10
l, r = 0, len(a)-1
pair = None
while l < r:
    total = a[l] + a[r]
    if total == target:
        pair = (a[l], a[r])
        break
    if total < target:
        l += 1
    else:
        r -= 1
print("6. Pair:", pair)

# 7. Remove duplicates from sorted list
a = [1, 1, 2, 2, 3, 4, 4]
pos = 1
for i in range(1, len(a)):
    if a[i] != a[pos-1]:
        a[pos] = a[i]
        pos += 1
print("7. Unique values:", a[:pos])

# 8. Container with most water
h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
l, r, best = 0, len(h)-1, 0
while l < r:
    best = max(best, min(h[l], h[r]) * (r-l))
    if h[l] < h[r]:
        l += 1
    else:
        r -= 1
print("8. Maximum water:", best)

# 9. Palindrome ignoring punctuation
s = "A man, a plan, a canal: Panama"
clean = "".join(c.lower() for c in s if c.isalnum())
print("9. Palindrome:", clean == clean[::-1])

# 10. Count positive-number subarrays with sum <= target
a, target = [1, 2, 1, 1], 4
left = total = count = 0
for right, x in enumerate(a):
    total += x
    while total > target:
        total -= a[left]
        left += 1
    count += right-left+1
print("10. Subarrays:", count)
