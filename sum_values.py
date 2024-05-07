class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_of_values(root):
    if root is None:
        return 0
    return root.value + sum_of_values(root.left) + sum_of_values(root.right)

# Приклад використання
# Створення дерева
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

# Знаходження суми всіх значень
total_sum = sum_of_values(root)
print("Сума всіх значень у дереві:", total_sum)
