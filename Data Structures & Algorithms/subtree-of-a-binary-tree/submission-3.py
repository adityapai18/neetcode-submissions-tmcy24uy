# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(root: Optional[TreeNode]) -> str:
            if root == None:
                return "$#"

            return ("$" + str(root.val) + serialize(root.left) + serialize(root.right))
        
        serialized_root = serialize(root)
        serialized_subRoot = serialize(subRoot)

        if serialized_subRoot in serialized_root:
            return True
        return False


        