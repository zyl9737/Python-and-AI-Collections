# 1维度梯度下降改变学习率演示
import numpy as np
import matplotlib.pyplot as plt

x = 10
lr = 0.8
result = [x]

for i in range(10):
    x -= lr*2*x
    result.append(x)
    
f_line = np.arange(-10, 10, 0.1)
plt.plot(f_line, [x**2 for x in f_line])
plt.plot(result, [x**2 for x in result], '-o')
plt.title(f"Learning Rate = {lr}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()