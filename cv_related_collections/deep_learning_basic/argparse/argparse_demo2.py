import argparse

parser = argparse.ArgumentParser(description="description")

parser.add_argument('--pa', '-a', action='store_true') # 当指定了--pa时，args.pa为True，否则为False
parser.add_argument('--pb', '-b', action="store_false")
args = parser.parse_args()
print(args)