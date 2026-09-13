# 54 - Advanced Bit Manipulation: 10 practical programs

# 1. Check kth bit
def kth_bit(n, k): return bool(n & (1 << k))
print("1. kth bit:", kth_bit(10, 1))

# 2. Remove rightmost set bit
def remove_rightmost(n): return n & (n - 1)
print("2. Remove bit:", remove_rightmost(12))

# 3. Get rightmost set bit
def rightmost_set(n): return n & -n
print("3. Rightmost set bit:", rightmost_set(12))

# 4. Count set bits from 0 to n
def count_bits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1): dp[i] = dp[i >> 1] + (i & 1)
    return dp
print("4. Counts:", count_bits(8))

# 5. Reverse 8 bits
def reverse_8bit(n):
    result = 0
    for _ in range(8):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
print("5. Reverse:", reverse_8bit(13))

# 6. XOR from 0 to n
def xor_range(n): return [n, 1, n + 1, 0][n % 4]
print("6. XOR range:", xor_range(10))

# 7. Find two unique numbers
def two_unique(nums):
    x = 0
    for n in nums: x ^= n
    bit = x & -x
    a = b = 0
    for n in nums:
        if n & bit: a ^= n
        else: b ^= n
    return a, b
print("7. Two unique:", sorted(two_unique([1,2,1,3,2,5])))

# 8. Generate Gray codes
def gray_codes(n): return [i ^ (i >> 1) for i in range(1 << n)]
print("8. Gray codes:", gray_codes(3))

# 9. Check opposite signs
def opposite_signs(a, b): return (a ^ b) < 0
print("9. Opposite signs:", opposite_signs(-5, 7))

# 10. Swap odd and even bits
def swap_odd_even(n):
    return ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
print("10. Swapped bits:", swap_odd_even(23))
