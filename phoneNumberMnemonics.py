# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:40:13 2021

@author: hungd
"""

def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    mnemonics = []
    phoneNumberMnemonicsHelper(0, phoneNumber, generateKeyPad(), "",  mnemonics)
    return mnemonics
    
def phoneNumberMnemonicsHelper(keyIndex, phoneNumber, keyPad, mnemonic, mnemonics):
    # Write your code here.
    if keyIndex >= len(phoneNumber):
        mnemonics.append(mnemonic)
        return
    
    for i in range(len(keyPad[phoneNumber[keyIndex]])):
        newMnemonic = mnemonic + keyPad[phoneNumber[keyIndex]][i]
        phoneNumberMnemonicsHelper(keyIndex + 1, phoneNumber, keyPad, newMnemonic, mnemonics)
        
def generateKeyPad():
    keyPad = {}
    keyPad["0"] = ["0"]
    keyPad["1"] = ["1"]
    keyPad["2"] = ["a", "b", "c"]
    keyPad["3"] = ["d", "e", "f"]
    keyPad["4"] = ["g", "h", "i"]
    keyPad["5"] = ["j", "k", "l"]
    keyPad["6"] = ["m", "n", "o"]
    keyPad["7"] = ["p", "q", "r", "s"]
    keyPad["8"] = ["t", "u", "v"]
    keyPad["9"] = ["w", "x", "y", "z"]
    return keyPad
  
phoneNumber = "1905"
phoneNumberMnemonics(phoneNumber)