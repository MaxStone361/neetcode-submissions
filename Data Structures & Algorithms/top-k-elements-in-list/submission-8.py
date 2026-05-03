class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #最小堆排序法
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        """ 省略版本：
        for i in nums:
            count[i] = 1 + count.get(i,0)
            # 创建键值对：dict.get(key, default)
        """

        minheap = []
        for num, cnt in count.items():
            heapq.heappush(minheap,(cnt, num))
            # 入堆方法：heapq.heappush(heap, item)，这里的节点是一个set。
            # 入堆后自动保持最小堆性质
            if len(minheap) > k:
                heapq.heappop(minheap)

        res = []
        for i in range(k):
        # 这里不能使用for i in minheap, 因为heappop()会改变堆结构
            res.append(heapq.heappop(minheap)[1])
        return res
 

        
        
            