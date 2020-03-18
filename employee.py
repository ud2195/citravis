#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:05:35 2020

@author: espm1854
"""

class employee():
    numberofemployees=0
    raise_amount=1.5
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        employee.numberofemployees+=1
        

    def fullname(self):
        print ('{} {}'.format(self.first,self.last))
        return self.first+' '+self.last
        
    def apply_raise(self):
        self.pay=self.pay*self.raise_amount
        return self.pay
    
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('_')
        return cls(first,last,pay)



            
 