class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        i=0
        j=len(height)-1
        while True:
            if i==j:
                break
            min_height=min(height[i],height[j])
            temp_area=abs(i-j)*min_height
            if temp_area>max_area:
                max_area=temp_area
            if min_height==height[i]:
                i+=1
            else:
                j-=1
        return max_area
