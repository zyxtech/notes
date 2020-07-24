class Solution:
    def groupAnagrams(self, strs) :
    #def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordChars = []
        wordandArrayNumber = {}
        for str in strs:

            wordChars = list(str)
            newWordChars = ''.join(sorted(wordChars))
            if wordandArrayNumber.get(newWordChars) is None :
                wordandArrayNumber[newWordChars] = []
                wordandArrayNumber[newWordChars].append(str)
            else:
                wordandArrayNumber[newWordChars].append(str)
        resultList = []
        for value in wordandArrayNumber.values():
            resultList.append(value)
        return resultList
if __name__ == '__main__':
    obj = Solution()
    print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


'''
from leetcode
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
'''        
