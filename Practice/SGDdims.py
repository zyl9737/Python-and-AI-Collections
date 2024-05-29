from matplotlib import pyplot as plt
import numpy as np

def loss_func(x1,x2):#定义目标函数
    return x1 ** 2 + 2 * x2 ** 2


x1, x2= -5, -2
eta = 0.4
num_epochs = 20
result = [(x1,x2)]
for epoch in range(num_epochs):
    gd1 = 2 * x1
    gd2 = 4 * x2
    x1 -= eta * gd1
    x2 -= eta * gd2
    result.append((x1,x2))
#print('x1:',result1)
#print('\n x2:'result2)
plt.figure(figsize=(8,4))
plt.plot(*zip(*result), '-o', color='#ff7f0e')
x1, x2 = np.meshgrid(np.arange(-5.5,1.0,0.1), np.arange(-3.0,1.0,0.1))
plt.contour(x1, x2, loss_func(x1,x2),colors='#1f77b4')
plt.title('learning rate ={}'.format(eta))
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
