class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #volume = min(h1,h2)*(index(h2)-index(h1))
        max=0
        i=0
        j=len(heights)-1
        while i<=j:
            vol = min(heights[i],heights[j])*(abs(j-i))
            if vol>max:
                max=vol
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max