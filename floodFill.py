# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

# Return the modified image after performing the flood fill.

 

# Example 1:


# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        h, w = len(image), len(image[0]) 
        visited = set()
		
        def dfs( r, c, src_color, new_color):
            
            if r < 0 or c < 0 or r >= h or c >= w or (r,c) in visited or image[r][c] != src_color:
                # Reject for invalid coordination, repeated traversal, or different color
                return
            
            # update color
            image[r][c] = new_color
            
            # mark current coordination as visited
            visited.add((r,c))
            
            # DFS to 4-connected neighbors
            dfs( r-1, c, src_color, new_color )
            dfs( r+1, c, src_color, new_color )
            dfs( r, c-1, src_color, new_color )
            dfs( r, c+1, src_color, new_color )
                 
        dfs(sr, sc, src_color = image[sr][sc], new_color = newColor)       
        return image
     
#     from collections import deque
# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
#         h, w = len(image), len(image[0])
        
#         src_color = image[sr][sc]
        
#         visited = set()
        
#         traversal_queue = deque( [(sr, sc)] )
        
#         while traversal_queue:
            
#             cur_r, cur_c = traversal_queue.popleft()
            
#             if cur_r < 0 or cur_r >= h or cur_c < 0 or cur_c >= w or (cur_r, cur_c) in visited or image[cur_r][cur_c] != src_color:
#                 continue
            
#             # update color
#             image[cur_r][cur_c] = newColor
            
#             # mark current coordinate as visited
#             visited.add( (cur_r, cur_c) )
            
#             # BFS to 4-connected neighbors
#             traversal_queue.append( (cur_r-1, cur_c) )
#             traversal_queue.append( (cur_r+1, cur_c) )
#             traversal_queue.append( (cur_r, cur_c-1) )
#             traversal_queue.append( (cur_r, cur_c+1) )
        
#         return image
