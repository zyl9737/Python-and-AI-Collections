# demo.py
import argparse

# 创建ArgumentParser()对象
parser = argparse.ArgumentParser()

# 添加参数
parser.add_argument('-o', '--output', action='store_true', 
    help="shows output")
# action = `store_true` 会将output参数记录为True
# type 规定了参数的格式
# default 规定了默认值
parser.add_argument('--lr', type=float, default=3e-5, help='select the learning rate, default=1e-3') 

parser.add_argument('--batch_size', type=int, required=True, help='input batch size')  
# 使用parse_args()解析函数
args = parser.parse_args()

if args.output:
    print("This is some output")
    print(f"learning rate:{args.lr} ")