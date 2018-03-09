import config
import tensorflow as tf
import model


def create_model():
	# prepare dataset
	c = config.getConfig()
	print(c.get('DATASET', 'DATA_PATH'))

	vocab_size = c.get('MODEL', 'VOCAB_SIZE')
	target_vocab_size = c.get('MODEL', 'TRAGET_VOCAB_SIZE')
	buckets = c.get('MODEL', 'BUCKETS')
	size = c.get('MODEL', 'SIZE')
	num_layers = c.get('MODEL', 'NUM_LAYERS')
	batch_size = c.get('MODEL', 'BATCH_SIZE')

	model = Seq2SeqModel(vocab_size, target_vocab_size, buckets, size=size, num_layers=num_layers, batch_size=batch_size)

def train():
	print("training bot..")

	# Seq2SeqModel
	model = create_model

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