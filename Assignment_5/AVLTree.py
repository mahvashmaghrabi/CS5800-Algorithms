from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    key: Any
    data: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None
    height: int = 0


class Tree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def avl_insert(self, key: Any, data: Any) -> None:

        node_n = Node(key=key, data=data)
        parent: Optional[Node] = None
        current: Optional[Node] = self.root
        while current:
            parent = current
            if node_n.key < current.key:
                current = current.left
            elif node_n.key > current.key:
                current = current.right

        node_n.parent = parent
        if parent is None:
            self.root = node_n
        else:
            if node_n.key < parent.key:
                parent.left = node_n
            else:
                parent.right = node_n

            if not (parent.left and parent.right):
                self.avl_insert_fixup(node_n)

    def left_rotate(self, x: Node) -> None:
        y = x.right
        if y:
            x.right = y.left
            if y.left:
                y.left.parent = x
            y.parent = x.parent
            if x.parent is None:
                self.root = y
            elif x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y

            y.left = x
            x.parent = y

            x.height = 1 + max(
                self.height(x.left), self.height(x.right)
            )
            y.height = 1 + max(
                self.height(y.left), self.height(y.right)
            )

    def right_rotate(self, x: Node) -> None:
        y = x.left
        if y:
            x.left = y.right
            if y.right:
                y.right.parent = x
            y.parent = x.parent
            if x.parent is None:
                self.root = y
            elif x == x.parent.right:
                x.parent.right = y
            else:
                x.parent.left = y

            y.right = x
            x.parent = y

            x.height = 1 + max(
                self.height(x.left), self.height(x.right)
            )
            y.height = 1 + max(
                self.height(y.left), self.height(y.right)
            )

    @staticmethod
    def height(node: Optional[Node]) -> int:
        if node:
            return node.height
        return -1

    def balance(self, node: Optional[Node]) -> int:
        if node:
            return self.height(node.left) - self.height(node.right)
        return -1

    def avl_insert_fixup(self, node_n: Node) -> None:
        parent = node_n.parent

        while parent:
            parent.height = 1 + max(
                self.height(parent.left), self.height(parent.right)
            )

            grandparent = parent.parent
            if grandparent:
                if self.balance(grandparent) > 1:

                    if self.balance(parent) >= 0:
                        self.right_rotate(grandparent)

                    elif self.balance(parent) < 0:
                        self.left_rotate(parent)
                        self.right_rotate(grandparent)
                    break
                elif self.balance(grandparent) < -1:

                    if self.balance(parent) <= 0:
                        self.left_rotate(grandparent)

                    elif self.balance(parent) > 0:
                        self.right_rotate(parent)
                        self.left_rotate(grandparent)
                    break
            parent = parent.parent
