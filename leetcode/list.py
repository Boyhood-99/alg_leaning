import math
import numpy as np
from typing import *

l = [k*k for k in range(10)]
print(l)
print(sorted([k*k for k in range(10)]))

class Array_():
    def search_(self, num, tgt):
        l, r = 0,len(num)-1
        while l<=r:
            middle = int(l+(r-l)/2)
            if num[middle] ==tgt:
                return middle
            if num[middle]>tgt:
                r == middle-1
            elif num[middle]<tgt:
                l ==middle+1
      
    def search(self, nums: List[int], target: int):
        l ,r = 0, len(nums)-1
        
        while True:
            m = int(l + (r -l)/2)
            if target == nums[m]:
                return m
            if target < nums[m]:
                r = m - 1
            if target > nums[m]:
                l = m + 1
            if l <= r:
                return None


class Array():

    def search(self,nums:List[int],target:int):  #二分查找，区间左闭右闭
        left,right=0,len(nums)-1
        while left<=right:
            middle=int(left+(right-left)/2)
            if nums[middle]>target:
                # nums=nums[left:middle-1]
                right=middle-1
            elif nums[middle]<target:
                # nums=nums[middle+1:right]
                left=middle+1
            else:
                return middle
        return -1        

    def sortedsquare(self,nums): #单调不减数组，求平方后排序，双指针法
        n=len(nums)
        a_=[-1]*n
        i,j,k=0,n-1,n-1
        while i<=j:
            l=math.pow(nums[i],2)
            r=math.pow(nums[j],2)
            if l <= r: 
                a_[k]=r
                j-=1
            else:
                a_[k]=l
                i+=1
            k-=1
        return a_
    def minsuuarraylen(self,nums,s):#最小长度子数组，暴力解法
        n=len(nums)
        #先设置长度，也可先设置起点
        for i in range(n):
            for j in range(n-i+1):
                result=0
                for k in range(i):
                    result+=nums[j+k]
                if result >=s:
                    return i,nums[j:j+i]
        return 0
    
    def minsuuarraylen_(self,nums,s):#最小长度子数组，双指针法滑动窗口
        n=len(nums)
        min_len=n+1
        sum=0
        i=0
        for j in range(n):
            sum+=nums[j]
            while sum>=s:    
                min_len=min(min_len,j-i+1)      
                sum-=nums[i]
                i+=1

        # if min_len<n+1:
        #     return min_len,nums[i-1:j+1]
        # else :
        #     return 0
        return min_len,nums[i-1:j+1] if min_len<n+1 else 0
    
    def generatematrix_(self,n):         #生成22
        nums=[[0]*n for _ in range(n)]
        startx,starty=0,0
        loop=n//2
       
        num=1

        for i in range(loop):
            loop_len=n-i-1
            for j in range(starty,loop_len):
                nums[startx][j]=num
                num+=1
            for j in range(startx,loop_len):
                nums[j][loop_len]=num
                num+=1

            for j in range(starty,loop_len):
                nums[loop_len][loop_len-(j-starty)]=num
                num += 1
            for j in range(startx,loop_len):
                nums[loop_len-(j-startx)][starty]=num
                num += 1
            startx += 1
            starty += 1

        if n%2 != 0:
            nums[loop][loop]=num

        return nums
    
    def generatematrix(self,n):         #生成22
        nums=[[0]*n for _ in range(n)]
        startx,starty=0,0
        loop=n//2
       
        num=1

        for i in range(loop):
            loop_len = n - 2*i
            for j in range(starty, starty+loop_len-1):
                nums[startx][j]=num
                num+=1
            for j in range(startx,startx+loop_len-1):
                nums[j][starty+loop_len-1]=num
                num+=1
            
            for j in range(starty+loop_len-1, starty,-1):
                
                nums[startx+loop_len-1][j]=num
                num += 1
            
            for j in range(startx+loop_len-1, startx,-1):
                nums[j][starty]=num
                num += 1
            

            startx += 1
            starty += 1

        if n%2 != 0:
            nums[loop][loop]=num

        return nums


a = list([1,3,2,])
a.reverse()
# print(a)
# print(i for i in list(range(6,1,-1)).reverse())
#实验
s=Array()
# a=s.sortedsquare(np.array([-1,0,2,5,6,7,8,9,11,13])-np.arange(10))#输入数组要求非递减

# a=s.minsuuarraylen([2,3,1,2,4,3],7)
# b=s.minsuuarraylen_([2,3,1,2,4,3],7)

# b=s.generatematrix_(5)
# print(b)





