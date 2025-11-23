class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=set(nums)
        return not len(n)==len(nums)
        