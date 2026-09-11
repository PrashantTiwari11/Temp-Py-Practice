"""50 - Bit Manipulation: 10 practical programs"""

# 1. Odd/even using bit
def is_odd(n): return (n & 1) == 1
print("1.", is_odd(17))

# 2. Get ith bit
def get_bit(n, i): return (n >> i) & 1
print("2.", get_bit(13, 2))

# 3. Set ith bit
def set_bit(n, i): return n | (1 << i)
print("3.", set_bit(8, 1))

# 4. Clear ith bit
def clear_bit(n, i): return n & ~(1 << i)
print("4.", clear_bit(15, 2))

# 5. Toggle ith bit
def toggle_bit(n, i): return n ^ (1 << i)
print("5.", toggle_bit(10, 0))

# 6. Count set bits
def count_set_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
print("6.", count_set_bits(29))

# 7. Power of two
def is_power_of_two(n): return n > 0 and (n & (n - 1)) == 0
print("7.", is_power_of_two(32))

# 8. Find unique number
def single_number(nums):
    result = 0
    for n in nums: result ^= n
    return result
print("8.", single_number([4,1,2,1,2]))

# 9. XOR swap
def xor_swap(a, b):
    a ^= b; b ^= a; a ^= b
    return a, b
print("9.", xor_swap(7, 12))

# 10. Generate subsets with bit masks
def all_subsets(items):
    return [[items[i] for i in range(len(items)) if mask & (1 << i)]
            for mask in range(1 << len(items))]
print("10.", all_subsets(["A","B","C"]))
