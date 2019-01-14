# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 20:01:57 2019

@author: LiuBL
"""
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i=len(bits)-2
        if len(bits)==1:#如果只有一个，一定是True（最后一个字符为一比特）
            return True
        elif bits[-1]==1:#如果最后一位是1，一定是False
            return False
        elif bits[-2]==0:#最后一位是0且倒数第二位也是0，一定是True
            return True
        else:#如果最后一位是0，倒数第二位是1，从后往前计算连续的1的个数，奇数为False,偶数为True。
            k=0
            while(i>=0):
                if bits[i]==1:
                    k=k+1
                else:
                    break
                i=i-1
            if k%2==0:
                return True
            else:
                return False
