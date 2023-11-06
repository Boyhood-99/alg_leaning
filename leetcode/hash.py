#字母异位词
from collections import defaultdict

class Hash():
    def isAnagram(self,s,t): #同形异位词
        record = [0]*26
        for i in s:
            record[ord(i)-ord('a')] += 1
        for i in t:
            record[ord(i)-ord('a')] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
        return True
    
    def intersection(self, list1, list2):
        val_dic = {}
        ans = []
        for i in list1:
            val_dic[i] = 1
        for i in list2:
            if i in val_dic.keys() and val_dic[i] == 1:
                ans.append(i)
                val_dic[i] == 0
        return ans
    
    def isHappy(self, n):
        record = set()
        sum = n
        while True:
            sum = self.getsum(sum)
            if sum == 1:
                return True
            if sum in record:
                return False
            else:
                record.add(sum)

    def getsum(self, n):   #求数字n各个位的平方和

        new_num = 0
        while n:
            n, r = divmod(n, 10)  #商和余数结合起来
            new_num += r ** 2
        return new_num
    
    def twoSum(self, list, target):#数组中，两数之和等于目标值的两个数的索引，map键值对 对应 数组数值和其索引
        record = dict()
        for index, value in enumerate(list):
            if target - value in record:
                return [record[target - value],index]
            record[value] = index
        return []
    
    def fourSum(self, list1, list2, list3, list4):#四个相同大小整数数组中四个数之和为0的索引元组个数
        record = dict()
        for i in list1:
            for j in list2:
                sum = i + j
                if sum in record:
                    record[sum] += 1
                else :
                    record[sum] = 1
        counter = 0
        for i in list3:
            for j in list4:
                _sum = -i - j
                if _sum in record:
                    counter += record[_sum]
        return counter

    def canConstruct(delf, str1, str2):#赎金信和杂志，字符串str1能否用str2字符来表示，不能重复

        ransom_count = [0]*26
        magazine = [0]*26

        for i in str1:
            ransom_count[ord(i) - 'a'] += 1
        for i in str2:
            magazine[ord(i) - 'a'] += 1

        return all(ransom_count[i] <= magazine[i] for i in range(26))

        
# s = Hash()

# print(s.isHappy(19))
# print(s.intersection([1,2,5],[7,5,4]))

