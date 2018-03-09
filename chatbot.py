import config


def train():
	print("training bot..")

	# retrieve config
	c = config.getConfig()
	print(c.get('DATASET', 'DATA_PATH'))

	# build the chatbot model
	## TODO 

	# Create a saver
	## Ref: https://www.tensorflow.org/api_docs/python/tf/train/Saver
	saver = tf.train.Saver()

	# run tf session
	## TODO
	### Ref: https://www.tensorflow.org/api_docs/python/tf/Session



def main():
	print("chatbot.py starts..")
	train()
	print("chatbot.py ends..")


if __name__ == '__main__':
    main()