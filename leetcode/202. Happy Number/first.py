class Solution(object):
    def getNextNum(self, n):
        copyn = n
        numList = []
        while copyn > 0 :
            numList.append( copyn % 10 )
            copyn = copyn/10
        returnNum = 0
        for num in numList:
            returnNum += num*num
        return returnNum
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        countCallgetNextNum = 0
        numUsedList = []
        while countCallgetNextNum <= 1000:
            if n in numUsedList:
                return False
            numUsedList.append(n)

            countCallgetNextNum += 1
            if countCallgetNextNum > 1000:
                return False
            print(n)
            n = self.getNextNum(n)
            if n == 1:
                return True
        return False


if __name__ == '__main__':
    obj = Solution()
    print(obj.isHappy(18))
