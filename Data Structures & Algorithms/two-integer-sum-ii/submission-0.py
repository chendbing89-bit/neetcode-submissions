class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i in range(0, len(numbers)):
            diff = target - numbers[i]
            if diff in d:
                return [d[diff] + 1, i + 1]
            d[numbers[i]] = i