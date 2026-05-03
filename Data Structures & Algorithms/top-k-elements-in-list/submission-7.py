class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #最小堆排序法
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        minheap = []
        for num, cnt in count.items():
        #一次性解包比二次解包更节省资源
            heapq.heappush(minheap,(cnt, num))
            if len(minheap) > k:
                heapq.heappop(minheap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res

        
        
            