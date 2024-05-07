class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max_value(root):
    current = root
    while current.right:
        current = current.right
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

# Знаходження найбільшого значення
max_value = find_max_value(root)
print("Найбільше значення у дереві:", max_value)
