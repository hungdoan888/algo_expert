# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:41:23 2021

@author: hungd
"""
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

    def addDirectReports(self, directReports):
        for directReport in directReports:
            self.directReports.append(directReport)


class orgInfoClass:
    def __init__(self):
        self.lowestCommonManager = None
        
def getOrgCharts():
    orgCharts = {}
    for letter in ALPHABET:
        orgCharts[letter] = OrgChart(letter)
    return orgCharts


def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    orgInfo = orgInfoClass()
    getLowestCommonManagerHelper(topManager, reportOne, reportTwo, orgInfo)
    return orgInfo.lowestCommonManager


def getLowestCommonManagerHelper(report, reportOne, reportTwo, orgInfo):
    # Write your code here.     
    numReportsInBranchMaster = 0
    if report == reportOne:
        numReportsInBranchMaster += 1
            
    if report == reportTwo:
        numReportsInBranchMaster += 1
    
    for i in range(len(report.directReports)):  
        numReportsInBranch = getLowestCommonManagerHelper(report.directReports[i], reportOne, reportTwo, orgInfo)
        numReportsInBranchMaster += numReportsInBranch
    

    if numReportsInBranchMaster == 2 and orgInfo.lowestCommonManager is None:
        orgInfo.lowestCommonManager = report
        
    return numReportsInBranchMaster
        
ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
orgCharts = getOrgCharts()
orgCharts["A"].addDirectReports([orgCharts["B"], orgCharts["C"]])
orgCharts["B"].addDirectReports([orgCharts["D"], orgCharts["E"]])
orgCharts["C"].addDirectReports([orgCharts["F"], orgCharts["G"]])
orgCharts["D"].addDirectReports([orgCharts["H"], orgCharts["I"]])

topManager = orgCharts["A"]
reportOne = orgCharts["E"]
reportTwo = orgCharts["I"]
getLowestCommonManager(topManager, reportOne, reportTwo)