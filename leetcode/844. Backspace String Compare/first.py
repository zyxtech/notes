class Solution:
    #def backspaceCompare(self, S: str, T: str) -> bool:
    def backspaceCompare(self, S, T):
        source = list(S)
        target = list(T)
        sourceStr = []
        targetStr = []
        for element in source:
            if element is '#':
                if len(sourceStr) > 0:
                    sourceStr.pop()
            else:
                sourceStr.append(element)
        for element in target:
            if element is '#':
                if len(targetStr) > 0:
                    targetStr.pop()
            else:
                targetStr.append(element)
        if ''.join( sourceStr ) == ''.join( targetStr ):
            return True
        else:
            return False
if __name__ == '__main__':
    obj = Solution()
    print(obj.backspaceCompare("a###b","b"))


'''
Approach #2: Two Pointer [Accepted]

Intuition

When writing a character, it may or may not be part of the final string depending on how many backspace keystrokes occur in the future.

If instead we iterate through the string in reverse, then we will know how many backspace characters we have seen, and therefore whether the result includes our character.

Algorithm

Iterate through the string in reverse. If we see a backspace character, the next non-backspace character is skipped. If a character isn't skipped, it is part of the final answer.

See the comments in the code for more details.

class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
'''
