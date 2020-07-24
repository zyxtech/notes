class Solution(object):
    def maxSubArray(self, nums):
        maxSumsbyIdentification = []
        i = 0
        max= nums[0]
        for num in nums :
            if i == 0 :
                maxSumsbyIdentification.append(num)
                i += 1
            else :
                if maxSumsbyIdentification[i-1] > 0 :
                    maxSumsbyIdentification.append(maxSumsbyIdentification[i-1] + num)
                else :
                    maxSumsbyIdentification.append(num)
                if maxSumsbyIdentification[i] > max :
                    max = maxSumsbyIdentification[i]
                i += 1
        return max
if __name__ == '__main__':
    obj = Solution()
    print(obj.maxSubArray([4,1,2,1,2]))
