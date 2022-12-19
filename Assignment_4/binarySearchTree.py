class Node:
    def __init__(self, key: int):
        self.val = key
        self.left = None
        self.right = None


def k_smallest(root: Node, k: int):
    y = []
    while root or y:
        while root:
            y.append(root)
            root = root.left
        root = y.pop()
        k -= 1
        if k == 0:
            break
        root = root.right
    return root.val


root = Node(41)
root.left = Node(20)
root.right = Node(65)
root.left.left = Node(11)
root.left.right = Node(29)
root.right.left = Node(50)
root.right.right = Node(91)
root.left.right.right = Node(32)
root.right.right.left = Node(72)
root.right.right.right = Node(99)

print(k_smallest(root, 4))
