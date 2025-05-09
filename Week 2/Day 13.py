print("\n\nDay 13\n")
print("\nChallenge (FACEprep): Delete the Middle Node of a Linked List")
print("Context: You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.\n\n")
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if not head.next:
            return None
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
solution = Solution()
new_head = solution.deleteMiddle(head)
# Print the modified linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")