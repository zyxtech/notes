class Solution(object):
    def moveZeroes(self, nums):
        zeroPositions = []
        zeroIndex = 0
        for num in nums:
            if num == 0 :
                zeroPositions.append(zeroIndex)
            zeroIndex += 1
        if len(zeroPositions) > 0 :
            currentIndex = 0
            currentMoveIndex = 0
            for zeroPosition in zeroPositions :
                currentMoveIndex = zeroPosition - currentIndex
                if len(zeroPositions) == (currentIndex + 1 ) :
                    while currentMoveIndex < ( len(nums) - len(zeroPositions) ):
                        nums[currentMoveIndex] = nums[ currentMoveIndex + currentIndex + 1 ]
                        currentMoveIndex += 1
                    setZeroCount = 0
                    while setZeroCount <= len(zeroPositions) - 1 :
                        nums[len(nums) + setZeroCount - len(zeroPositions)] = 0
                        setZeroCount += 1
                    currentIndex += 1
                elif len(zeroPositions) > (currentIndex + 1 ) :
                    while currentMoveIndex < ( zeroPositions[ currentIndex + 1 ] - currentIndex - 1 ) :
                        nums[ currentMoveIndex ] = nums [ currentMoveIndex + currentIndex + 1 ]
                        currentMoveIndex += 1
                    currentIndex += 1
        return nums
if __name__ == '__main__':
    obj = Solution()
    #print(obj.moveZeroes([4,1,0,1,2]))
    print(obj.moveZeroes([0,1,0,3,12]))





#Move Zeroes
#https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3286/
