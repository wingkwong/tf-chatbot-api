import config
import tensorflow as tf
import ast
from model import Seq2SeqModel

# retrieve config.ini
c = config.getConfig()

def create_model():
	print("creating seq2seq model..")
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
	model = Seq2SeqModel(source_vocab_size, target_vocab_size, buckets, size, num_layers, max_gradient_norm, batch_size, learning_rate, learning_rate_decay_factor)
	return model

def check_saver_restore(sess, saver):
	checkpoint_dir = c.get('SAVER', 'SAVER_PATH')
	ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
	if ckpt and ckpt.model_checkpoint_path:
		print('restoring the previously trained parameters')
		saver.restore(sess, ckpt.model_checkpoint_path)
	else:
		pass

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
		# init variables 
		sess.run(tf.global_variables_initializer())
		# check if restoring variables is needed
		## Ref: https://www.tensorflow.org/programmers_guide/saved_model
		check_saver_restore(sess, saver)



def main():
	print("chatbot.py starts..")
	train()
	print("chatbot.py ends..")


if __name__ == '__main__':
    main()