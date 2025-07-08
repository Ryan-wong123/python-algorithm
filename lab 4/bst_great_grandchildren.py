import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if node is None:
                return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return node

        self.root = _insert(self.root, key)

    def find(self, key):
        def _find(node, key):
            if node is None or node.key == key:
                return node
            return _find(node.left, key) if key < node.key else _find(node.right, key)

        return _find(self.root, key)

    def printTree(self, node=None, level=0, prefix="Root: "):
        # Only set to self.root on the *initial* call
        if node is None and level == 0:
            node = self.root
        if node is None:
            return

        self.printTree(node.right, level + 1, "R--- ")
        print(" " * (level * 4) + prefix + node.key)
        self.printTree(node.left, level + 1, "L--- ")
        
    def getGreatGrandChildren(self, n):
        def count_level(node, level):
            if node is None:
                return 0
            if level == 0:
                return 1
            return count_level(node.left, level - 1) + count_level(node.right, level - 1)
        return count_level(n, 3)


def main():
    try:
        if sys.stdin.isatty():
            print("Enter a node key: ")
            nodekey = input().strip()
            print("Enter the keys of the tree separated by spaces: ")
            keys = input().strip().split()
        else:
            print("Enter a node key: ", end="")
            input_lines = sys.stdin.read().strip().split('\n')
            if len(input_lines) >= 2:
                nodekey = input_lines[0].strip()
                print("Enter the keys of the tree separated by spaces: ", end="")
                keys = input_lines[1].strip().split()
            else:
                print("Insufficient input provided.")
                return
    except Exception:
        print("Error reading input.")
        return

    # Create BST and insert nodes
    tree = BST()
    for key in keys:
        tree.insert(key)

    #tree.printTree()

    # Get Great GrandChildren
    node_f = tree.find(nodekey)
    print(f"Great-grandchildren of {nodekey}: {tree.getGreatGrandChildren(node_f)}")


if __name__ == "__main__":
    main()