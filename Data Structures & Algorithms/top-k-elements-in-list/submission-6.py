class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        minheap = []
        for num, cnt in count.items():
            heapq.heappush(minheap, (cnt, num))
            if len(minheap) > k:
                heapq.heappop(minheap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res
        
            