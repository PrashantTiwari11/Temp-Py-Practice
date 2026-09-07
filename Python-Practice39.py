# Day 9 - 33: Heap and Priority Queue
import heapq

# 1. Create a min heap
def make_heap(nums):
    heap = nums[:]
    heapq.heapify(heap)
    return heap

# 2. Push into heap
def push(heap, value):
    heapq.heappush(heap, value)

# 3. Pop smallest
def pop_smallest(heap):
    return heapq.heappop(heap) if heap else None

# 4. Three smallest
def three_smallest(nums):
    return heapq.nsmallest(3, nums)

# 5. Three largest
def three_largest(nums):
    return heapq.nlargest(3, nums)

# 6. Priority queue
def priority_queue():
    q = [(2, "Normal"), (1, "Urgent"), (3, "Low")]
    heapq.heapify(q)
    return [heapq.heappop(q) for _ in range(len(q))]

# 7. Kth smallest
def kth_smallest(nums, k):
    values = heapq.nsmallest(k, nums)
    return values[-1] if values else None

# 8. Merge sorted lists
def merge_lists(lists):
    return list(heapq.merge(*lists))

# 9. Top scores
def top_scores(scores, n):
    return heapq.nlargest(n, scores)

# 10. Heap sort
def heap_sort(nums):
    heap = make_heap(nums)
    return [heapq.heappop(heap) for _ in range(len(heap))]

if __name__ == "__main__":
    h = make_heap([7, 2, 9, 1, 5])
    push(h, 3)
    print(h, pop_smallest(h))
    print(three_smallest([7,2,9,1,5]))
    print(three_largest([7,2,9,1,5]))
    print(priority_queue())
    print(kth_smallest([8,2,6,1,9], 3))
    print(merge_lists([[1,4,7],[2,5,8],[3,6,9]]))
    print(top_scores([78,92,85,99,88], 3))
    print(heap_sort([5,1,8,3,2]))
