import tensorflow as tf

def model_creation():
	model = tf.keras.Sequential()
	model.add(tf.keras.layers.Conv1D(40, 10, activation='relu'))
	return model

def main():
	model = model_creation()
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

if __name__ == "__main__":
	print("running main.py script")
	main()
