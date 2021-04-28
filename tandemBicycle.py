# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 18:21:04 2021

@author: hungd
"""

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    if fastest:
        return tandemFastest(redShirtSpeeds, blueShirtSpeeds)
    else:
        return tandemSlowest(redShirtSpeeds, blueShirtSpeeds)

def tandemFastest(red, blue):
	redLeft = 0
	redRight = len(red) - 1
	blueLeft = 0
	blueRight = len(blue) - 1
	
	tandemSum = 0
	while redLeft <= redRight and blueLeft <= blueRight:
		if red[redRight] >= blue[blueRight]:
			tandemSum += red[redRight]
			redRight -= 1
			blueLeft += 1
		else:
			tandemSum += blue[blueRight]
			redLeft += 1
			blueRight -= 1
	return tandemSum

def tandemSlowest(red, blue):
	tandemSum = 0
	for i in range(len(red)):
		if red[i] >= blue[i]:
			tandemSum += red[i]
		else:
			tandemSum += blue[i]
	return tandemSum

redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = False
tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
