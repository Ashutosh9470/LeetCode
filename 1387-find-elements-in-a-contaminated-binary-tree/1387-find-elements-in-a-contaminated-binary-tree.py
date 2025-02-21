

class FindElements:
    def __init__(self, root):
        self.recoveredValues = set()
        root.val = 0
        self.recoverTree(root)

    def recoverTree(self, root):
        if not root:
            return
        self.recoveredValues.add(root.val)
        if root.left:
            root.left.val = 2 * root.val + 1
            self.recoverTree(root.left)
        if root.right:
            root.right.val = 2 * root.val + 2
            self.recoverTree(root.right)

    def find(self, target):
        return target in self.recoveredValues