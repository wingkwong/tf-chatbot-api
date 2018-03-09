import config
import tensorflow as tf
import ast
from model import Seq2SeqModel


def create_model():
	print("creating seq2seq model..")
	# retrieve config.ini
	c = config.getConfig()
	# prepare dataset
	source_vocab_size = c.getint('MODEL', 'SOURCE_VOCAB_SIZE')
	target_vocab_size = c.getint('MODEL', 'TRAGET_VOCAB_SIZE')
	buckets = ast.literal_eval(c.get('MODEL', 'BUCKETS'))
	size = c.getint('MODEL', 'SIZE')
	num_layers = c.getint('MODEL', 'NUM_LAYERS')
	max_gradient_norm = c.getint('MODEL', 'MAX_GRADIENT_NORM')
	batch_size = c.getint('MODEL', 'BATCH_SIZE')
	learning_rate = c.getint('MODEL', 'LEARNING_RATE')
	learning_rate_decay_factor = c.getint('MODEL', 'LEARNING_RATE_DECAY_FACTOR')
	# build seq2seq model
	return model = Seq2SeqModel(source_vocab_size, target_vocab_size, buckets, size, num_layers, max_gradient_norm, batch_size, learning_rate, learning_rate_decay_factor)

def train():
	print("training bot..")

	# Seq2SeqModel
	model = create_model()

	# Create a saver
	## Ref: https://www.tensorflow.org/api_docs/python/tf/train/Saver
	saver = tf.train.Saver()

	# Run tf session
	## Ref: https://www.tensorflow.org/api_docs/python/tf/Session
	with tf.Session() as sess:
		print('Running tf session')
		sess.run(tf.global_variables_initializer())


def main():
	print("chatbot.py starts..")
	train()
	print("chatbot.py ends..")


if __name__ == '__main__':
    main()