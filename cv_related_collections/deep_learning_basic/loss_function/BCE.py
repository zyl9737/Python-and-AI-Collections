import torch.nn as nn
import torch

# torch.nn.BCELoss(weight=None, size_average=None, reduce=None, reduction='mean')
m = nn.Sigmoid()
loss = nn.BCELoss()
input = torch.randn(3, requires_grad=True)
target = torch.empty(3).random_(2) # 上限是2，所以随机的值是0或1
output = loss(m(input), target)
output.backward()
print('BCELoss损失函数的计算结果为',output)