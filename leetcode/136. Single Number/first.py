class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numAndCount = {}
        for num in nums:
            if num not in numAndCount :
                numAndCount[num] = 1
            elif num in numAndCount :
                numAndCount[num] = 2
        for num in numAndCount:
            if numAndCount[num] == 1:
                return num
        return None
    def __init__(self):
        self.data = []
if __name__ == '__main__':
    obj = Solution()
    print(obj.singleNumber([4,1,2,1,2]))

#https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/
'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''
