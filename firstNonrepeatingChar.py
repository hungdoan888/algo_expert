def firstNonRepeatingCharacter(string):
    repeatingChars = {}
    for i in range(len(string)):
        if string[i] not in repeatingChars:
            repeatingChars[string[i]] = 1
        else:
            repeatingChars[string[i]] += 1

    for i in range(len(string)):
        if repeatingChars[string[i]] == 1:
            return i
    return -1
    
string = "abcdcaf"
firstNonRepeatingCharacter(string)