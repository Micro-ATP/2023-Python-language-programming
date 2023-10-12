def sortCharFrequency(s):

    charFrequency = {}
    
    for char in s:
        if char in charFrequency:
            charFrequency[char] += 1
        else:
            charFrequency[char] = 1

    sortedStr = ''.join(sorted(s, key=lambda char: (-charFrequency[char], char)))
    
    return sortedStr

inputStr = "tree"
sortedResult = sortCharFrequency(inputStr)
print("Sorted Result:", sortedResult)
