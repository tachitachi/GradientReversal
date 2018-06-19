import tensorflow as tf

def flip_gradient(x, l=1.0):
	positive_path = tf.stop_gradient(x * tf.cast(1 + l, tf.float32))
	negative_path = -x * tf.cast(l, tf.float32)
	return positive_path + negative_path