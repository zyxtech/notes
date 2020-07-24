class Solution:
    def groupAnagrams(self, strs) :
    #def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordChars = []
        wordandArrayNumber = {}
        for str in strs:
            wordChars = []
            for char in str:
                wordChars.append( char )
            if ( len( wordChars ) >= 2 ):
                for i in range(len(wordChars)-2 , -1,-1):
                    changedInCompare = False
                    for j in range( 0 , i + 1 ):
                        if wordChars[j] > wordChars[j+1]:
                            tempValue = wordChars[j]
                            wordChars[j] = wordChars[j+1]
                            wordChars[j+1] = tempValue
                            changedInCompare = True
                    if changedInCompare is False :
                        break
            newWordChars = self.convert(wordChars)
            if wordandArrayNumber.get(newWordChars) is None :
                wordandArrayNumber[newWordChars] = []
                wordandArrayNumber[newWordChars].append(str)
            else:
                wordandArrayNumber[newWordChars].append(str)
        resultList = []
        for value in wordandArrayNumber.values():
            resultList.append(value)
        return resultList
    def convert(self,s):
        new = ""
        for x in s:
            new += x
        return new
if __name__ == '__main__':
    obj = Solution()
    print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
