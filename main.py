# -*- coding: utf-8 -*-
# @Author: huyz1117
# @Date:   2019-01-23 21:39:48
# @Last Modified by:   huyz1117
# @Last Modified time: 2019-01-24 16:29:52

import argparse
from utils import *

from DCGAN import DCGAN


def parse_args():
	desc = 'Implement DCGAN with TensorFLow'
	parser = argparse.ArgumentParser(description=desc)
	parser.add_argument('--phase', type=str, default='train', help='train or test ?')
	parser.add_argument('--dataset', type=str, default='celeba', help='celeba')

	parser.add_argument('--epoch', type=int, default=20, help='The number of epochs to train')
	parser.add_argument('--batch_size', type=int, default=64, help='The size of batch per gpu')
	parser.add_argument('--learning_rate', type=float, default=0.0002, help='The learning rate for optimizer')
	parser.add_argument('--z_dim', type=int, default=100, help='Dimension of noise vector')
	parser.add_argument('--print_freq', type=int, default=300, help='Print frequence')
	parser.add_argument('--image_size', type=int, default=64, help='The size of the output images to produce')
	parser.add_argument('--c_dim', type=int, default=3, help='Dimension of the image color')
	parser.add_argument('--output_height', type=int, default=64, help='The size of output image')
	parser.add_argument('--output_width', type=int, default=64, help='The width of output image')

	parser.add_argument('--sample_num', type=int, default=64, help='The number of sample images')
	parser.add_argument('--test_num', type=int, default=10, help='The number of images generated by the test')

	parser.add_argument('--checkpoint_dir', type=str, default='checkpoint', help='Directory name to save the checkpoints')
	parser.add_argument('--log_dir', type=str, default='logs', help='Directory name to save the training logs')
	parser.add_argument('--result_dir', type=str, default='results', help='Directory name to save the generated images')
	parser.add_argument('--sample_dir', type=str, default='samples', help='Directory name to save the samples on training')

	return check_args(parser.parse_args())


''' checking arguments '''
def check_args(args):
	# --checkpoint_dir
	check_folder(args.checkpoint_dir)

	# --result_dir
	check_folder(args.result_dir)

	# --sample_dir
	check_folder(args.sample_dir)

	# --log_dir
	check_folder(args.log_dir)

	# --epoch
	try:
		assert args.epoch >= 1
	except:
		print('Number of epochs must be larger than or equal to one!')

	# --batch_size
	try:
		assert args.batch_size >= 1
	except:
		print('Number of epochs must be larger than or equal to one!')

	return args


def main():
    # parse arguments
    args = parse_args()
    if args is None:
      exit()

    # open session
    with tf.Session() as sess:
        gan = DCGAN(sess, args)

        # build graph
        gan.build_model()

        # show network architecture
        show_all_variables()

        if args.phase == 'train' :
            # launch the graph in a session
            gan.train()

            # visualize learned generator
            gan.visualize_results(args.epoch - 1)

            print(" [*] Training finished!")

        if args.phase == 'test' :
            gan.test()
            print(" [*] Test finished!")

if __name__ == '__main__':
    main()
