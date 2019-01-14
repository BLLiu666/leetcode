# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 21:06:21 2019

@author: LiuBL
"""
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        inta=int(a,2)
        intb=int(b,2)
        intc=inta+intb
        bi=bin(intc)[2:]
        return bi

                
            
        
