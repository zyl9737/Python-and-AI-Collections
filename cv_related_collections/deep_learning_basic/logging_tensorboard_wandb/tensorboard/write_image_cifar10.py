import torchvision
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter


transform_train = transforms.Compose(
    [transforms.ToTensor()])
transform_test = transforms.Compose(
    [transforms.ToTensor()])

train_data = datasets.CIFAR10("/data/zyl/", train=True, download=True, transform=transform_train)
test_data = datasets.CIFAR10("/data/zyl/", train=False, download=True, transform=transform_test)
train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = DataLoader(test_data, batch_size=64)

images, labels = next(iter(train_loader))
 
# 仅查看一张图片
# writer = SummaryWriter('./pytorch_tb')
# writer.add_image('images[0]', images[0])
# writer.close()
 
# 将多张图片拼接成一张图片，中间用黑色网格分割
# create grid of images
# writer = SummaryWriter('./pytorch_tb')
# img_grid = torchvision.utils.make_grid(images)
# writer.add_image('image_grid', img_grid)
# writer.close()
 
# 将多张图片直接写入
writer = SummaryWriter('./pytorch_tb')
writer.add_images("images",images,global_step = 0)
writer.close()