# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

arr=[1,2,31,23,45,87,-16,-4,0,11,2]
number=len(arr)

#a_ans
for i in range(1,number):
    val=arr[i] + arr[i-1] 
    print(val, end=", ")
    continue
print (" ")

#a_ans2
ans=[]
for i in range (0,number):
    if (i==0):
        val=arr[i]
        print(val, end=" ")
    else:
        val=arr[i]+arr[i-1]
        print(val, end=" ")
      
print(" ")
        
#b_ans
#c_ans
for i in range (0, number):
    if (arr[i] > arr[i+1]):
        max= arr[i]
    else:
        max= arr[i+1]
        
print(max)
#e_ans
midvalue=int((number+1)/2)
print(arr[midvalue])