import time
from typing import List
class Travel():
    def __init__(self, nums) -> None:
        self.nums = nums
        self.count = 0
        self.m = len(self.nums)
        self.n = len(self.nums[0])
    def dfs(self, x, y):
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 四个方向
        i,j =x,y
        if self.nums[x][y] !=1:
            return
        
        # for i in range(m):
        #     for j in range(n):
        # self.nums[x][y] = 0
        # for d in dirs:
        #     nextx = x + d[0]
        #     nexty = y + d[1]
        #     if nextx < 0 or nextx >= self.m or nexty < 0 or nexty >= self.n:  # 越界了，直接跳过
        #         continue
        #     self.dfs(nextx, nexty)
        
        self.nums[x][y] = 0
        if i-1 >= 0:
            self.dfs( i-1, j)
        if i+1 <self.m:
            self.dfs( i+1, j)
        if j-1 >= 0:
            self.dfs( i, j-1)
        if j+1 <self.n:
            self.dfs( i, j+1)


        # if self.nums[x][y] == 0:
        #         return  # 终止条件：访问过的节点 或者 遇到海水
        # self.nums[x][y] = 0
        # for d in dirs:
        #     nextx = x + d[0]
        #     nexty = y + d[1]
        #     if nextx < 0 or nextx >= self.m or nexty < 0 or nexty >= self.n:  # 越界了，直接跳过
        #         continue
        #     self.dfs(nextx, nexty)
    def numIsland(self, ):
        for x in range(self.m):
            for y in range(self.n):
                if self.nums[x][y] == 1:
                    self.count += 1
                    self.dfs(x, y)
        return self.count

tr = Travel([[0,1,0,1],
        [0,1,0,1],
        [1,0,1,0]]
       )
print(tr.numIsland())

