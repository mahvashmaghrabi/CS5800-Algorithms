class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Insertion Sort
def insertionSort(head):
    linkedlist_head = Node(head)
    cur = head

    while cur:
        pointer1 = linkedlist_head
        pointer2 = linkedlist_head.next

        while pointer2:
            if cur.val < pointer2.val:
                break
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        var = cur.next

        cur.next = pointer2
        pointer1.next = cur

        cur = var

    return linkedlist_head.next


def constructLinkedList(nums):
    if not nums:
        return None
    head = Node(nums[0])
    cur = head
    for v in nums[1:]:
        new_node = Node(v)
        cur.next = new_node
        cur = new_node
    return head


def printLinkedList(head):
    cur = head
    l = []
    while cur:
        print(cur.val)
        l.append(cur.val)
        cur = cur.next
    print(l)


l = constructLinkedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
printLinkedList(l)


l = insertionSort(l)
printLinkedList(l)
