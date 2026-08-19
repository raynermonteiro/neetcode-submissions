# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            #If Empty leef node then is valid BST
            if not node:
                return True
            
            #if current node val is within the bounds
            if not low < node.val < high:
                return False
            
            # Update bounds for children:
            # Left child must be smaller than the current node's value (updates high bound)
            # Right child must be larger than the current node's value (updates low bound)
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        return validate(root, float('-inf'), float('inf'))
        