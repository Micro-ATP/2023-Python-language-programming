def processTextFile(inputFilePath, outputFilePath):
    with open(inputFilePath, 'r', encoding='utf-8') as inputFile:
        data = inputFile.read()

    lineCount = len(data.split('\n'))

    wordCount = len(data.split())

    charCount = len(data)

    resultStr = f"行数: {lineCount}\n单词数: {wordCount}\n字符数: {charCount}"

    with open(outputFilePath, 'w', encoding='utf-8') as outputFile:
        outputFile.write(resultStr)

    print("处理完成，结果已写入到{}文件中。".format(outputFilePath))


inputFilePath = 'Homework\Lecture8-Homework（files readind and writing)\input1.txt'
outputFilePath = 'Homework\Lecture8-Homework（files readind and writing)\output1.txt'
processTextFile(inputFilePath, outputFilePath)
