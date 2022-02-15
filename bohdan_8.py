class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0
        stack = []
        
        while(root or stack):
            if root:
                stack.append(root)
                root = root.left
                if root and root.left is None and root.right is None:
                    result += root.val
            else:
                root = stack.pop()
                root = root.right
        
        return result