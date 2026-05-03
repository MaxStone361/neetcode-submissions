class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #建立一个字典用于计数
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            # 堆的push操作: heapq(heap, item)
            # 这个堆的节点是一个二元组, 以(count[], num)的形式存储计数对
            if len(heap) > k:
                heapq.heappop(heap)
            # heappush会在push过程中自动排序保持最小堆性质, 因此超出k个元素会自动推出

        res = []
        for i in range(k):
                res.append(heapq.heappop(heap)[1])
        return res