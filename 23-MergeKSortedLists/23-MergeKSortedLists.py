# Last updated: 7/9/2026, 9:03:48 AM
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # For printing the list (optional)
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return str(result)

class Solution:
    def mergeKLists(self, lists):
        heap = []
        counter = 0  # Unique counter to avoid comparison issues

        # Initialize heap with the head of each list
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

        dummy = ListNode()
        current = dummy

        while heap:
            val, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next
