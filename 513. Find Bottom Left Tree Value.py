class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        row = [root]
        while row:
            temp = []
            for node in row:
                print(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                row = temp
            else:
                return row[0].val


node7 = TreeNode(7)
node6 = TreeNode(6)
node5 = TreeNode(5, node7, None)
node4 = TreeNode(4)
node3 = TreeNode(3, node5, node6)
node2 = TreeNode(2, node4, None)
node1 = TreeNode(1, node2, node3)
s = Solution()
s.findBottomLeftValue(node1)
