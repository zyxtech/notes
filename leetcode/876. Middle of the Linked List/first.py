# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
#    def middleNode(self, head: ListNode) -> ListNode:
    def middleNode(self, head) :
        count = 0
        headCopy = head
        if headCopy is not None:
            while headCopy is not None:
                print(headCopy.val)
                count += 1
                headCopy = headCopy.next
        count = int(count / 2)
        currentCount = 0
        if head is not None:
            while head is not None and ( currentCount < count  ) :
                currentCount += 1
                head = head.next
            return head
            #print(allValues)
        else:
            return None
if __name__ == '__main__':
    head = None
    next = None
    for element in [1,2,3,4,5]:
        if head is None:
            head = ListNode(element)
            next = head
        else:
            next.next = ListNode(element)
            next = next.next
    solution = Solution()
    print( solution.middleNode( head ).val )


    #print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


'''
class Solution(object):
    def middleNode(self, head):
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) / 2]

class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
'''
