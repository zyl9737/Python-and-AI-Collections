import argparse

parser = argparse.ArgumentParser(description="description")

parser.add_argument('-gf', '--girlfriend', choices=['jingjing', 'lihuan'])
parser.add_argument('food')
parser.add_argument('--house', type=int, default=0)

args = parser.parse_args()
print('args :',args)
print('girlfriend :', args.girlfriend)
print('food :', args.food)
print('house :', args.house)