import torch
import torch.nn as nn
from torchsummary import summary
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = nn.Sequential(nn.Conv2d(3, 16, kernel_size=3, padding=1),
                      nn.BatchNorm2d(16),
                      nn.ReLU())
model.to(device) # 因为报错所以加上，输入和模型都要在同一个设备上
print(summary(model, (3, 224, 224), 8))



