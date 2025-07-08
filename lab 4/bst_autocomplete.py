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

    def autocomplete(self, prefix):
        result = []

        def _inorder(node):
            if node is None:
                return
            _inorder(node.left)
            if node.key.startswith(prefix):
                result.append(node.key)
            _inorder(node.right)

        _inorder(self.root)
        return result

def main():
    prefix = input("Enter prefix: ").strip().lower()
    words = input("Enter the words of the tree separated by spaces: ").strip().split()
    words = [word.lower() for word in words]

    tree = BST()
    for word in words:
        tree.insert(word)

    matches = tree.autocomplete(prefix)
    print(f"Autocomplete results for prefix '{prefix}':")
    for word in matches:
        print(word)

if __name__ == "__main__":
    main()
