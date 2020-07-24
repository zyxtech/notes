class Solution(object):
    def maxProfit(self, prices):
    #def maxProfit(self, prices: List[int]) -> int:
        index = 0
        value = 0
        while index <= ( len( prices ) - 1 ):
            low = 0
            high = 0
            while ( ( index + 1) <= len( prices ) - 1 ) and ( prices[index] >= prices [index + 1]):
                index += 1
            low = prices[index]
            index += 1
            while ( ( index + 1) <= len( prices ) - 1 ) and ( prices[index] <= prices [index + 1] ):
                index += 1
            if index <= (len( prices ) - 1):
                high = prices[index]
                value += high - low
        return value
if __name__ == '__main__':
    obj = Solution()
    #print(obj.moveZeroes([4,1,0,1,2]))
    #print(obj.maxProfit([0,1,0,3,12]))
    #print(obj.maxProfit([0,1,3]))
    print(obj.maxProfit([7,6,4,3,1]))
    #print(obj.maxProfit([1,2,3,4,5]))
    #print(obj.maxProfit([7,1,5,3,6,4]))
    #print(obj.maxProfit([1,2,3,4,5]))

    #print(obj.maxProfit([0,1]))
#refer
#Best Time to Buy and Sell Stock II
#https://www.youtube.com/watch?v=Zz3do4oQw70
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/
#https://medium.com/@monisha.mary.mathew/best-time-to-buy-and-sell-stock-ii-b8c27bd9e54d
