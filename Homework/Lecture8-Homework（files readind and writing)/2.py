import pandas as pd
import numpy as np

def analyzeIrisData(inputFilePath, outputFilePath):
    irisData = pd.read_csv(inputFilePath)
    print("Iris 数据:")
    print(irisData.head())

    numericColumns = irisData.select_dtypes(include=[np.number])

    meanValues = numericColumns.mean()
    stdDevValues = numericColumns.std()

    print("\n均值:")
    print(meanValues)

    print("\n标准差:")
    print(stdDevValues)

    with open(outputFilePath, 'w') as outputFile:
        outputFile.write("均值:\n")
        outputFile.write(str(meanValues) + '\n\n')

        outputFile.write("标准差:\n")
        outputFile.write(str(stdDevValues) + '\n')

    print(f"统计分析结果已保存到 {outputFilePath}")

inputFilePath = 'Homework\Lecture8-Homework（files readind and writing)\Iris.csv'
outputFilePath = 'Homework\Lecture8-Homework（files readind and writing)\irisStatisticalAnalysisResults.txt'

analyzeIrisData(inputFilePath, outputFilePath)
