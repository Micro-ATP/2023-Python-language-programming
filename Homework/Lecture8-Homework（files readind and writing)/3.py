import os

def createAndWriteFile(directory, filename, data):
    filePath = os.path.join(directory, filename)

    with open(filePath, 'w') as file:
        file.write(data)
        
def readFileWithExceptionHandling(filePath):
    try:
        with open(filePath, 'r') as file:
            content = file.read()
            print("文件内容：")
            print(content)
    except FileNotFoundError:
        print(f"错误：文件 '{filePath}' 不存在。")
    except Exception as e:
        print(f"发生错误：{e}")

directory = 'Homework\Lecture8-Homework（files readind and writing)'
filename = 'example3.txt'
dataToWrite = "why not rust"

createAndWriteFile(directory, filename, dataToWrite)

readFileWithExceptionHandling(os.path.join(directory, filename))

nonExistentFilePath = os.path.join(directory, 'nonExistentFile.txt')
readFileWithExceptionHandling(nonExistentFilePath)
