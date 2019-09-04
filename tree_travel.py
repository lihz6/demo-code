from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderTraversal(root: TreeNode) -> List[int]:
    if root is None:
        return []
    list = []
    list += inorderTraversal(root.left)
    list.append(root.val)
    list += inorderTraversal(root.right)
    return list


# 建立子树
#    6
#   / \
#  4   7
n4 = TreeNode(4)
n7 = TreeNode(7)
n6 = TreeNode(6)
n6.left = n4
n6.right = n7


# 建立子树
#    14
#   /
#  13
n13 = TreeNode(13)
n14 = TreeNode(14)
n14.left = n13


# 建立子树
#    3
#   / \
#  1   6
#     / \
#    4   7
n1 = TreeNode(1)
n3 = TreeNode(3)
n3.left = n1
n3.right = n6


# 建立子树
#  10
#   \
#    14
#   /
#  13
n10 = TreeNode(10)
n10.right = n14


# 建立子树
#        8
#       / \
#      /   \
#     /     \
#    3       10
#   / \       \
#  1   6       14
#     / \     /
#    4   7   13
n8 = TreeNode(8)
n8.left = n3
n8.right = n10

# python3 tree_travel.py
print(inorderTraversal(n8))

# 运行分析
# inorderTraversal(n8)
#     root: n8 (此时root是n8, 下同)
#     list: [] (此时list为[], 下同)
#     L: inorderTraversal(n8.left) (L为inorderTraversal(root.left)返回的结果，下同)
#         root: n3
#         list: []
#         L: inorderTraversal(n3.left)
#             root: n1
#             list: []
#             L: inorderTraversal(n1.left)
#                 root: None
#                 ruturn: []
#             list: list + L -> []
#             list: list.append(root.val) -> [1]
#             R: inorderTraversal(root.right)
#                  root: None
#                  return: []
#             list: list + R -> [1]
#             return: list -> [1]
#         list: list + L -> [1]
#         list: list.append(n3.val) -> [1, 3]
#         R: inorderTraversal(n3.right) (R为inorderTraversal(root.right)返回的结果，下同)
#             root: n6
#             list: []
#             L: inorderTraversal(n6.left)
#                 root: n4
#                 list: []
#                 L: inorderTraversal(n4.left)
#                     root: None
#                     return: []
#                 list: list + L -> []
#                 list: list.append(n4.val) -> [4]
#                 R: inorderTraversal(n4.right)
#                     root: None
#                     return: []
#                 list: list + R -> []
#                 return: list -> [4]
#             list: list + L -> [4]
#             list: list.append(n6.val) -> [4, 6]
#             R: inorderTraversal(n6.right)
#                 root: n7
#                 list: []
#                 L: inorderTraversal(n7.left)
#                     root: None
#                     return: []
#                 list: list + L -> []
#                 list: list.append(n7.val) -> [7]
#                 R: inorderTraversal(n7.right)
#                     root: None
#                     return: []
#                 list: list + R -> []
#                 return: list -> [7]
#             list: list + R -> [4, 6, 7]
#             return: list -> [4, 6, 7]
#         list: list + R -> [1, 3, 4, 6, 7]
#     list: list.append(n8.val) -> [1, 3, 4, 6, 7, 8]
#     R: inorderTraversal(n8.right)
#          root: n10
#          list: []
#          L: inorderTraversal(n10.left)
#              root: None
#              return: []
#          list: list + L -> []
#          list: list.append(n10.val) -> [10]
#          R: inorderTraversal(n10.right)
#              root: n14
#              list: []
#              L: inorderTraversal(n14.left)
#                  root: n13
#                  list: []
#                  L: inorderTraversal(n13.left)
#                      root: None
#                      return: []
#                  list: list + L -> []
#                  list: list.append(n13.val) -> [13]
#                  R: inorderTraversal(n13.right)
#                      root: None
#                      return: []
#                  list: list + R -> [13]
#                  return: list -> [13]
#              list: list.append(n14.val) -> [13, 14]
#              R: inorderTraversal(n14.right)
#                  root: None
#                  return: []
#              list: list + R -> [13, 14]
#              return: list -> [13, 14]
#          list: list + R -> [10, 13, 14]
#      list: list + R -> [1, 3, 4, 6, 7, 8, 10, 13, 14]
#      return: list -> [1, 3, 4, 6, 7, 8, 10, 13, 14]
# 运行结果
# [1, 3, 4, 6, 7, 8, 10, 13, 14]

