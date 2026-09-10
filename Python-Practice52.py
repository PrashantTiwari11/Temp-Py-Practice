# Day 12 - 47: Greedy Algorithms

# 1. Activity selection
activities = [(1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]
activities.sort(key=lambda x: x[1])
chosen = []
end = -1
for start, finish in activities:
    if start >= end:
        chosen.append((start, finish))
        end = finish
print("1. Selected activities:", chosen)

# 2. Fractional knapsack
items = [(60,10), (100,20), (120,30)]
capacity = 50
items.sort(key=lambda x: x[0]/x[1], reverse=True)
value = 0
for v, w in items:
    take = min(w, capacity)
    value += take * v / w
    capacity -= take
    if capacity == 0:
        break
print("2. Maximum value:", value)

# 3. Greedy coin change
amount = 93
coins = [50,20,10,5,2,1]
used = []
for coin in coins:
    while amount >= coin:
        amount -= coin
        used.append(coin)
print("3. Coins:", used)

# 4. Assign cookies
children = [1,2,3]
cookies = [1,1]
i = j = satisfied = 0
while i < len(children) and j < len(cookies):
    if cookies[j] >= children[i]:
        satisfied += 1
        i += 1
    j += 1
print("4. Satisfied:", satisfied)

# 5. Minimum railway platforms
arr = [900,940,950,1100,1500,1800]
dep = [910,1200,1120,1130,1900,2000]
arr.sort()
dep.sort()
i = j = current = best = 0
while i < len(arr):
    if arr[i] <= dep[j]:
        current += 1
        best = max(best, current)
        i += 1
    else:
        current -= 1
        j += 1
print("5. Platforms:", best)

# 6. Jump Game
nums = [2,3,1,1,4]
reach = 0
for i, jump in enumerate(nums):
    if i > reach:
        break
    reach = max(reach, i+jump)
print("6. Can reach end:", reach >= len(nums)-1)

# 7. Gas station circuit
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
if sum(gas) < sum(cost):
    start = -1
else:
    start = tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
print("7. Starting station:", start)

# 8. Minimum arrows for balloons
points = [(10,16), (2,8), (1,6), (7,12)]
points.sort(key=lambda x: x[1])
arrows = 0
end = None
for start, finish in points:
    if end is None or start > end:
        arrows += 1
        end = finish
print("8. Arrows:", arrows)

# 9. Partition labels
s = "ababcbacadefegdehijhklij"
last = {c:i for i,c in enumerate(s)}
parts = []
start = end = 0
for i, c in enumerate(s):
    end = max(end, last[c])
    if i == end:
        parts.append(i-start+1)
        start = i+1
print("9. Partition sizes:", parts)

# 10. Maximum non-overlapping meetings
meetings = [(0,30), (5,10), (15,20), (25,35), (40,50)]
meetings.sort(key=lambda x: x[1])
count = 0
end = -1
for start, finish in meetings:
    if start >= end:
        count += 1
        end = finish
print("10. Maximum meetings:", count)
