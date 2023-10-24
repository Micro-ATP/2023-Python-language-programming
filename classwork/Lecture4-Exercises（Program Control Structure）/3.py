import time

# 获取当前日期和时间信息
current_time = time.localtime()
current_year = current_time.tm_year
current_month = current_time.tm_mon
current_day = current_time.tm_mday

# 判断是否是闰年
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# 不同月份的天数（未考虑闰年）
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 累加前几个月的天数
day_of_year = sum(days_in_month[:current_month - 1])

# 如果是闰年且当前月份大于2月，需要考虑2月多一天
if is_leap_year(current_year) and current_month > 2:
    day_of_year += 1

# 加上当前月份的日期
day_of_year += current_day

print(f"今天是今年的第 {day_of_year} 天。")
