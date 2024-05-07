class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_min_value(root):
    current = root
    while current.left:
        current = current.left
    return current.value

# Приклад використання
# Створення дерева
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

# Знаходження найменшого значення
min_value = find_min_value(root)
print("Найменше значення у дереві:", min_value)
