# 1. 读取文件，计算平均温度
file_path = 'C:\\Users\\19440\\Documents\\GitHub\\2023-Python-language-programming\\Homework\\Exercise matplotlib\\sensor.txt'

# 初始化变量
total_temperature = 0
record_count = 0

# 打开文件并逐行读取
with open(file_path, 'r', encoding='utf-8') as file:
    # 跳过文件头
    file.readline()
    
    # 逐行读取数据
    for line in file:
        # 分割每行数据
        data = line.strip().split(',')
        
        # 获取温度数据（假设温度在第三列）
        temperature = float(data[2])
        
        # 累加温度和记录数
        total_temperature += temperature
        record_count += 1

# 计算平均温度
average_temperature = total_temperature / record_count

# 输出平均温度
print(f'平均温度为：{average_temperature:.2f} 摄氏度')

# 2. 绘制温度变化图表
import matplotlib.pyplot as plt

# 重新打开文件以获取所有数据
with open(file_path, 'r', encoding='utf-8') as file:
    # 跳过文件头
    file.readline()
    
    # 初始化列表以存储时间和温度数据
    times = []
    temperatures = []
    
    # 逐行读取数据
    for line in file:
        # 分割每行数据
        data = line.strip().split(',')
        
        # 获取时间和温度数据
        time = data[0] + ' ' + data[1]
        temperature = float(data[2])
        
        # 添加到列表中
        times.append(time)
        temperatures.append(temperature)

# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(times, temperatures, marker='o', linestyle='-', color='b')
plt.title('温度变化图表')
plt.xlabel('时间')
plt.ylabel('温度（摄氏度）')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# 显示图表
plt.show()
