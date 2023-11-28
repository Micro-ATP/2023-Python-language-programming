import numpy as np

scores = np.random.randint(0, 100, size=(3, 5, 5, 4))

class_avg = np.mean(scores, axis=(1, 2, 3))
print("每个班级的平均分：", class_avg)

student_total = np.sum(scores, axis=(2, 3))
print("每个学生的总分：", student_total)

subject_std = np.std(scores, axis=(0, 1, 3))
print("每个科目的标准差：", subject_std)