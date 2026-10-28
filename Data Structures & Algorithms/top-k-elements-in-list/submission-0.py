class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seq = defaultdict(int)
        for num in nums:
            seq[num] += 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in seq.items():
            bucket[value].append(key)
        res = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res



        