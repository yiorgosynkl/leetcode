################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200511
# Problem link      : https://leetcode.com/problems/flood-fill/
################################################################

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n_rows = len(image)
        n_cols = len(image[0])
        startColor = image[sr][sc]
        if startColor == newColor:
            return image
        
        def fill(row, col):
            if image[row][col] == startColor:
                image[row][col] = newColor
                if row > 0: fill(row - 1, col)
                if row < n_rows - 1: fill(row + 1, col)
                if col > 0: fill(row, col - 1)
                if col < n_cols - 1: fill(row, col + 1)     
        
        fill(sr, sc)
        return image
    
# consice form
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]
        def traverse(row, col):
            if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != orig_color:
                return
            image[row][col] = newColor
            [traverse(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]
        if orig_color != newColor:
            traverse(sr, sc)
        return image