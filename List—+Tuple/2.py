def sortWordsInList(wordList):

    sortedList = sorted(wordList)
    return sortedList

wordList = ["Windows", "MacOS", "Ubuntu", "archLinux", "QTS"]

sortedWordList = sortWordsInList(wordList)

print("Sorted List of Words:", sortedWordList)


# 额外了解：
# 起初我对arch在最后感到不解，经过查询资料后我了解到sorted()的排序方式是按照字母的ASCII码顺序进行升序排序，而字母的ASCII码顺序是根据字符的Unicode码点值来确定的，因此大写字母会排在小写字母之前。
# 在深入了解后，我发现可以通过:
# sortedList = sorted(wordList, key=str.lower)
# 来消除对大小写的区分