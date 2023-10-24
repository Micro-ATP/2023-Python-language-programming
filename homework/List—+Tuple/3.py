def mergeIntervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    together = [intervals[0]]

    for interval in intervals[1:]:
        currentStart, currentEnd = interval
        previousStart, previousEnd = together[-1]

        if currentStart <= previousEnd:

            together[-1] = [previousStart, max(previousEnd, currentEnd)]
        else:

            together.append(interval)

    return together


# 本来是不会写的，但是查阅了了一些资料了解到了key=lambda x: x[N] 可以用来比较每个子列表或元组的第N个元素
# 就写了函数，没调用