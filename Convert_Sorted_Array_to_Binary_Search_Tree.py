# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper( self, nums: List[int], sIdx: int, eIdx: int ) -> Optional[TreeNode]:

        if sIdx == eIdx:
            node = TreeNode( nums[sIdx] )
            return node
        
        midIdx = sIdx + ( eIdx - sIdx )//2

        leftNode = None
        if midIdx > sIdx:
            leftNode = self.helper( nums, sIdx, midIdx - 1 )

        rightNode = None
        if eIdx > midIdx:
            rightNode = self.helper( nums, midIdx + 1, eIdx )

        node = TreeNode( nums[midIdx], leftNode, rightNode )
        return node


    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if len( nums) == 0:
            return None

        return self.helper( nums, 0, len(nums) - 1 )
