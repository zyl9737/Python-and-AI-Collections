import torch
import torch.nn as nn

net1 = nn.Sequential(nn.Linear(32, 64), nn.ReLU())
net2 = nn.ModuleList([nn.Linear(32, 64), nn.ReLU()])
net3 = nn.ModuleDict({'linear': nn.Linear(32, 64), 'act': nn.ReLU()})

x = torch.randn(8, 3, 32)
# print(net1(x).shape) # 只有Sequential可以直接调用，自带forward方法
# print(net2(x).shape)
# print(net3(x).shape)

# 为nn.ModuleList添加forward方法
# class My_Model(nn.Module):
#     def __init__(self):
#         super(My_Model, self).__init__()
#         self.model = nn.ModuleList([nn.Linear(32, 64), nn.ReLU()])
    
#     def forward(self, x):
#         for layer in self.model:
#             x = layer(x)
#         return x

# net = My_Model()

# out = net(x)
# print(out.shape)    

# 把nn.ModuleList转换为nn.Sequential
# module_list = nn.ModuleList([nn.Linear(32, 64), nn.ReLU()])
# net = nn.Sequential(*module_list)
# print(net(x).shape)

# 把nn.ModuleDict转换为nn.Sequential
# module_dict = nn.ModuleDict({'linear': nn.Linear(32, 64), 'act': nn.ReLU()})
# net = nn.Sequential(*module_dict.values())
# print(net(x).shape)