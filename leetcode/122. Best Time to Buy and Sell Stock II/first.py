class Solution(object):
    globalPrices = []
    resultLists = []
    def maxProfit(self, prices):
    #def maxProfit(self, prices: List[int]) -> int:
        self.globalPrices = prices
        self.getsubBest([])
        return self.getValue()
    def getValue(self):
        maxValue = 0
        buyPrice = 0
        sellPrice = 0
        currentIndex = 0
        currentSumValue = 0
        for resultList in self.resultLists:
            if currentSumValue > maxValue :
                maxValue = currentSumValue
            currentIndex = 0
            currentSumValue = 0

            for element in resultList :
                if currentIndex % 2 == 0 :
                    buyPrice = self.globalPrices[element]
                else:
                    sellPrice = self.globalPrices[element]
                    currentSumValue += ( sellPrice - buyPrice )
                currentIndex += 1
        if currentSumValue > maxValue :
            maxValue = currentSumValue
        return maxValue


    def getsubBest(self, opList):
        #buy
        if len( opList ) % 2 == 0 :
            if len(opList) == 0 :
                index = 0
            else:
                index = opList[ len(opList) - 1 ] + 1
            if index == len(self.globalPrices) - 1 :
                #print(opList)
                #self.resultLists.append(opList)
                newopList = opList.copy()
                if len( newopList ) > 0:
                    self.resultLists.append( newopList )
                return
            while index < ( len(self.globalPrices) - 1 ):
                newopList = opList.copy()
                newopList.append( index )

                self.getsubBest( newopList )
                index += 1
            return

        else:
            index = opList [ len(opList) -1 ] + 1
            buyPrice = self.globalPrices[ index - 1 ]

            while index <= len(self.globalPrices) - 1 :
                if ( self.globalPrices[ index ] ) > buyPrice and (index < len(self.globalPrices) - 1 ) :
                    newopList = opList.copy()
                    newopList.append( index )
                    #opList.append( index )
                    self.getsubBest(newopList)
                if index == len(self.globalPrices) - 1 :
                    newopList = opList.copy()
                    if self.globalPrices[ index ] > buyPrice :
                        newopList.append( index )
                    else:
                        del newopList[ len(opList) - 1 ]
                    if len( newopList ) > 0 :
                        self.resultLists.append( newopList )
                    return
                index += 1
            return
        return
if __name__ == '__main__':
    obj = Solution()
    #print(obj.moveZeroes([4,1,0,1,2]))
    #print(obj.maxProfit([0,1,0,3,12]))
    #print(obj.maxProfit([0,1,3]))
    #print(obj.maxProfit([7,6,4,3,1]))
    #print(obj.maxProfit([1,2,3,4,5]))
    #print(obj.maxProfit([7,1,5,3,6,4]))
    print(obj.maxProfit([1,2,3,4,5]))

    #print(obj.maxProfit([0,1]))
    print(obj.resultLists)
