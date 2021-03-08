# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:43:15 2021

@author: hungd
"""

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # Write your code here.
    calendar1 = putDailyBoundsinCalendar(dailyBounds1, calendar1)
    calendar2 = putDailyBoundsinCalendar(dailyBounds2, calendar2)
    calendar = mergeCalendars(calendar1, calendar2)
    possibleTimes = getPossibleMeetingTimes(calendar, meetingDuration)
    return possibleTimes
    

def convertTimeToMinutes(time):
    timeArray = time.split(":")
    minutes = int(timeArray[0]) * 60 + int(timeArray[1])
    return minutes

    
def getPossibleMeetingTimes(calendar, duration):
    possibleTimes = []
    for i in range(1, len(calendar)):
        meeting1End = convertTimeToMinutes(calendar[i - 1][1])
        meeting2Start = convertTimeToMinutes(calendar[i][0])
        if meeting1End >= meeting2Start:
            continue
        if meeting2Start - meeting1End >= duration:
            possibleTimes.append([calendar[i - 1][1], calendar[i][0]])
    return possibleTimes
            
    
def mergeCalendars(calendar1, calendar2):
    idx1 = 0
    idx2 = 0
    calendar = []
    while idx1 < len(calendar1) or idx2 < len(calendar2):
        if idx1 >= len(calendar1):
            calendar.append(calendar2[idx2])
            idx2 += 1
        elif idx2 >= len(calendar2):
            calendar.append(calendar1[idx1])
            idx1 += 1
        else:
            calendar1StartTime = convertTimeToMinutes(calendar1[idx1][0])
            calendar2StartTime = convertTimeToMinutes(calendar2[idx2][0])
            if calendar1StartTime == calendar2StartTime:
                calendar1StopTime = convertTimeToMinutes(calendar1[idx1][1])
                calendar2StopTime = convertTimeToMinutes(calendar2[idx2][1])
                if calendar1StopTime <= calendar2StopTime:
                    calendar.append(calendar1[idx1])
                    idx1 += 1
                else:
                    calendar.append(calendar2[idx2])
                    idx2 += 1
            elif calendar1StartTime < calendar2StartTime:
                calendar.append(calendar1[idx1])
                idx1 += 1
            else:
                calendar.append(calendar2[idx2])
                idx2 += 1
                
    # Ensuring end times come after end times
    for i in range(1, len(calendar)):
        presentStop = convertTimeToMinutes(calendar[i][1])
        pastStop = convertTimeToMinutes(calendar[i - 1][1])
        if pastStop > presentStop:
            calendar[i][1] = calendar[i - 1][1]
    return calendar
    
    
def putDailyBoundsinCalendar(dailyBounds, calendar):
    beforeWork = ["0:00", dailyBounds[0]]
    afterWork = [dailyBounds[1], "24:00"]
    calendar.insert(0, beforeWork)
    calendar.append(afterWork)
    return calendar


calendar1 = [
  ["10:00", "10:30"],
  ["10:45", "11:15"],
  ["11:30", "13:00"],
  ["14:15", "16:00"],
  ["16:00", "18:00"]
]

dailyBounds1 = ["9:30", "20:00"]

calendar2 = [
  ["10:00", "11:00"],
  ["12:30", "13:30"],
  ["14:30", "15:00"],
  ["16:00", "17:00"]
]

dailyBounds2 = ["9:00", "18:30"]

meetingDuration = 15
calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
