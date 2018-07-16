# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):
	ans1= (-b+math.sqrt(b*b-4*a*c))/(2*a)
	ans2= (-b-math.sqrt(b*b-4*a*c))/(2*a)
	return ans1,ans2
x,y=quadratic(2, 3, 1)
print(x,y)
