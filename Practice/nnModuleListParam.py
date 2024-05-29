import torch.nn as nn

net = nn.ModuleList([nn.Linear(32, 64), nn.ReLU()])

for name,param in net.named_parameters():
    print(name, param.size())