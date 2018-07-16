# -*- coding: utf-8 -*-
def findMinAndMax(L):
	if len(L)==0:
		return none,none
	else:
		min=max=L[0]
		for x in L :
			if min>x :
				min=x
			if max<x :
				max=x
		return min,max
list=[7,8,9,1,2,10]
x,y=findMinAndMax(list)
print(x,y)