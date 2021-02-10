# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:53:01 2021

@author: hungd
"""

def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    surplus = 0
    minSurplus = 0
    starting_city = 0
    fuel = [i * mpg for i in fuel]
    for i in range(len(distances)):
        surplus += (fuel[i] - distances[i])
        if surplus < minSurplus:
            minSurplus = surplus
            starting_city = (i + 1) % len(distances)
        print(surplus)
    return starting_city
        
            
distances = [30, 25, 5, 100, 40]
fuel = [3, 2, 1, 0, 4]
mpg = 20
validStartingCity(distances, fuel, mpg)