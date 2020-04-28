import os
import argparse
from collections import defaultdict


def extnum_func(args):
	dataset = defaultdict(lambda:0)

	for root, dirs, files in os.walk(args.srcdir):
		for srcname in files:
			name, ext = os.path.splitext(srcname)
			dataset[ext] += 1

	print(args.srcdir)

	dataset = sorted(dataset.items(), key=lambda kv: kv[1], reverse=True)

	for ext, num in dataset:
		print('  ', ext, num)


def print_help(parser):
	def wrapper(args):
		parser.print_help()

	return wrapper


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--srcdir', default='D:\\Projects\\Project-IGI1\\game\\')
	parser.set_defaults(func=print_help(parser))

	subpar = parser.add_subparsers()
	extnum = subpar.add_parser('extnum', help='Count files by extension')
	extnum.set_defaults(func=extnum_func)


	args = parser.parse_args()
	args.func(args)


if __name__ == '__main__':
	main()
