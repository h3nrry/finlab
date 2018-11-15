# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:36:44 2018

@author: MTK06810
"""

# Function: Split word from c with n-words
# Usages: [] = split_at(s,c)
def split_at(s,c):
    return s.split(c)
    

#Remove CR
def rm_cr(s):
    return s.replace('\n','')

#string hex to integer
def strhex2int(s):
    return int(str(s[:-2]),16)

#string hex '0x' to integer
def strhex0x2int(s):
    return int(str(s[1][:-2]),16)

#hex2int
def hex2int(val):
    return int(val,16)

def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

#Convert hex string into binary string
def strhex2strbin(s):
    hex2bin_lut = ['0000','0001','0010','0011',
                   '0100','0101','0110','0111',
                   '1000','1001','1010','1011',
                   '1100','1101','1110','1111']
    sbin=''
    for i in range(len(s)):
        sbin += hex2bin_lut[int(s[i],base=16)]
    return sbin
    
    