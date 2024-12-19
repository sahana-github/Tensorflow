# # import Tensorflow 2
import tensorflow as tf
 
# placeholders are not executable immediately so we need to disable eager exicution in TF 2 not in 1
tf.compat.v1.disable_eager_execution()
 
# # Create Placeholder
a = tf.compat.v1.placeholder(dtype=tf.float32, shape=(400,400))
a
 
a.dtype
 
a.shape
 
a.name
 
b = tf.compat.v1.placeholder(dtype=tf.float32, shape=(400,400))
b
 
# # Perform mathematical operation with placeholder
c = tf.add(a, b)
c
 
# # Create Numpy Array
import numpy as np
ones_array = np.ones((400,400), np.float32)
ones_array
 
# # Execute Tensorflow Placeholder using session
with tf.compat.v1.Session() as sess:
    d = sess.run(c, feed_dict={a:ones_array, b:ones_array})
d
 
# type of variable
type(d)
