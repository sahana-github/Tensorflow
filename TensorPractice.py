	
tf.ones(shape, dtype=tf.dtypes.float32, name=None) -> Return Ones Tensor

# Import TensorFlow 2
import tensorflow as tf
 
# create ones tensor
ones_2dt = tf.ones((2,2), tf.float32)
ones_2dt
 
ones_3dt = tf.ones((2,2,4), tf.float32)
ones_3dt



tf.ones_like(input, dtype=None, name=None) -> Return Ones Tensor

# Import TensorFlow 2
import tensorflow as tf
 
# create ones tensor from input
 
cont_2dt = tf.constant([[1,2,3],[4,5,6]])
cont_2dt
 
ones_2dt_from_cont = tf.ones_like(cont_2dt, tf.float32)
ones_2dt_from_cont
 
var_2dt_from_var = tf.Variable([[1,2,3],[4,5,6]])
var_2dt_from_var
 
ones_2dt_from_var = tf.ones_like(var_2dt_from_var, tf.int32)
ones_2dt_from_var

tf.ones_initializer()

# Import TensorFlow 2
import tensorflow as tf
 
# create ones tensor TensorFlow variable from the input
 
def ones_variable(shape, dtype, initializer):
    return tf.Variable(initializer(shape=shape, dtype=dtype))
 
ones_variable((2,2), tf.float32,  tf.ones_initializer())
 
ones_variable((2,3,5), tf.int32,  tf.ones_initializer())
