################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200703
# Problem link      : https://leetcode.com/problems/prison-cells-after-n-days/
################################################################

class Solution:
    # def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
    #     # first and last switch to 0
    #     prv, nxt = cells, [0]*8 # the first and last elements become 0 and the remain that way   
    #     for _ in range((N-1) % 14 + 1): 
    #         nxt[0], nxt[7] = 0, 0
    #         for idx in range(1,7):
    #             nxt[idx] = int(prv[idx-1] == prv[idx+1])
    #         prv, nxt = nxt, prv
    #     return prv

#     def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
#         def step(cells):
#             return [0] + [int(cells[i-1] == cells[i+1]) for i in range(1,7)] + [0]
#         cells, times = step(cells), N-1
#         for _ in range(times % 14): # cycle that repeats every 14 steps
#             cells = step(cells)
#         return cells

#     def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
#         def step(cells):
#             return [0] + [int(cells[i-1] == cells[i+1]) for i in range(1,7)] + [0]
#         def get_id(cells):
#             return int(''.join([str(num) for num in cells[1:7]]) , 2)
        
#         cells, times = step(cells), N-1
#         ids = { get_id(cells) }
#         while times > 0:
#             cells = step(cells)
#             cid = get_id(cells)
#             if cid in ids: # the cycle started (the length of loop can be 1, 7, or 14, so the lcm = 14)
#                 while times - len(ids) > 0: 
#                     times -= len(ids)
#                 ids = set()
#             else:
#                 ids.add(cid)
#             times -= 1
#         return cells
    
#     # solutions by lee215
#     def prisonAfterNDays(self, cells, N):
#         seen = {str(cells): N}
#         while N:
#             seen.setdefault(str(cells), N)
#             N -= 1
#             cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
#             if str(cells) in seen:
#                 N %= seen[str(cells)] - N
#         return cells
    
    def prisonAfterNDays(self, cells, N):
        N -= max(N - 1, 0) / 14 * 14
        for i in range(N):
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
        return cells
    
# explain 14: https://math.stackexchange.com/questions/3311568/why-does-this-pattern-repeat-after-14-cycles-instead-of-256-can-you-give-a-proo
    