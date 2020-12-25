################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20201225
# Problem link      : https://leetcode.com/problems/diagonal-traverse/
################################################################

class Solution:
#     def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
#         # the sum of indices of each diagonal is constant
#         rs, cs = len(matrix), len(matrix[0])    # rows, cols
#         ans = []
#         for s in range(rs+cs-1):    # 0, 1, ..., rs - 1 + cs - 1
#             inds = [(r,s-r) for r in range(rs) if 0 <= s-r < cs]                
#             for r, c in inds:        
#                 ans.append(matrix[r][c])
#         return ans
            

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []: return []
        rs, cs = len(matrix), len(matrix[0])    # rows, cols
        ans = []
        for s in range(rs+cs-1):    # 0, 1, ..., rs - 1 + cs - 1
            rng = range(rs) if s % 2 == 1 else reversed(range(rs))
            inds = [(r,s-r) for r in rng if 0 <= s-r < cs]          
            for r, c in inds:        
                ans.append(matrix[r][c])
        return ans
    
	# def findDiagonalOrder(self, matrix):
	# 	"""
	# 	:type matrix: List[List[int]]
	# 	:rtype: List[int]
	# 	"""
	# 	d={}
	# 	#loop through matrix
	# 	for i in range(len(matrix)):
	# 	for j in range(len(matrix[i])):
	# 			#if no entry in dictionary for sum of indices aka the diagonal, create one
	# 	if i + j not in d:
	# 	d[i+j] = [matrix[i][j]]
	# 	else:
	# 			#If you've already passed over this diagonal, keep adding elements to it!
	# 	d[i+j].append(matrix[i][j])
	# 	# we're done with the pass, let's build our answer array
	# 	ans= []
	# 	#look at the diagonal and each diagonal's elements
	# 	for entry in d.items():
	# 		#each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
	# 		#snake time, look at the diagonal level
	# 	if entry[0] % 2 == 0:
	# 			#Here we append in reverse order because its an even numbered level/diagonal. 
	# 	[ans.append(x) for x in entry[1][::-1]]
	# 	else:
	# 	[ans.append(x) for x in entry[1]]
	# 	return ans
    
    def findDiagonalOrder(self, matrix):
        m, n = len(matrix), len(matrix and matrix[0])
        return [matrix[i][d-i]
                for s in range(m+n-1)
                for i in range(max(0, s-n+1), min(s+1, m))[::s%2*2-1]]
        # 0 <= i < m and 
        # 0 <= j < n ==> 0 <= s-i < n ==> s-n < i <= s ==> s-n+1 <= i < s+1
        # [::s%2*2-1] this means if s%2==1 then [::1] (stay same) and if s%2==0 then [::-1] (reverse)



    # # official solution    
    # def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
    #     # Check for an empty matrix
    #     if not matrix or not matrix[0]:
    #         return []
        
    #     # The dimensions of the matrix
    #     N, M = len(matrix), len(matrix[0])
        
    #     # Incides that will help us progress through 
    #     # the matrix, one element at a time.
    #     row, column = 0, 0
        
    #     # As explained in the article, this is the variable
    #     # that helps us keep track of what direction we are
    #     # processing the current diaonal
    #     direction = 1
        
    #     # Final result array that will contain all the elements
    #     # of the matrix
    #     result = []
        
    #     # The uber while loop which will help us iterate over all
    #     # the elements in the array.
    #     while row < N and column < M:
            
    #         # First and foremost, add the current element to 
    #         # the result matrix. 
    #         result.append(matrix[row][column])
            
    #         # Move along in the current diagonal depending upon
    #         # the current direction.[i, j] -> [i - 1, j + 1] if 
    #         # going up and [i, j] -> [i + 1][j - 1] if going down.
    #         new_row = row + (-1 if direction == 1 else 1)
    #         new_column = column + (1 if direction == 1 else -1)
            
    #         # Checking if the next element in the diagonal is within the
    #         # bounds of the matrix or not. If it's not within the bounds,
    #         # we have to find the next head. 
    #         if new_row < 0 or new_row == N or new_column < 0 or new_column == M:
                
    #             # If the current diagonal was going in the upwards
    #             # direction.
    #             if direction:
                    
    #                 # For an upwards going diagonal having [i, j] as its tail
    #                 # If [i, j + 1] is within bounds, then it becomes
    #                 # the next head. Otherwise, the element directly below
    #                 # i.e. the element [i + 1, j] becomes the next head
    #                 row += (column == M - 1)
    #                 column += (column < M - 1)
    #             else:
                    
    #                 # For a downwards going diagonal having [i, j] as its tail
    #                 # if [i + 1, j] is within bounds, then it becomes
    #                 # the next head. Otherwise, the element directly below
    #                 # i.e. the element [i, j + 1] becomes the next head
    #                 column += (row == N - 1)
    #                 row += (row < N - 1)
                    
    #             # Flip the direction
    #             direction = 1 - direction        
    #         else:
    #             row = new_row
    #             column = new_column
                        
    #     return result                 
