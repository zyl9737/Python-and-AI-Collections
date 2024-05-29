# 导入必要库
import random
import numpy as np
import torch
import config

opt = config.get_options()

manual_seed = opt.seed
num_workers = opt.workers
batch_size = opt.batch_size
lr = opt.lr
niters = opt.niters
checkpoint_path = opt.checkpoint_path

# 随机数的设置，保证复现结果
def set_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True

...


if __name__ == '__main__':
	set_seed(manual_seed)
	for epoch in range(niters):
		train(model,lr,batch_size,num_workers,checkpoint_path)
		val(model,lr,batch_size,num_workers,checkpoint_path)