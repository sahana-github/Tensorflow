# # Import TensorFlow
import tensorflow as tf
 
# # Create Tensor
tf.Variable(1)
 
a = tf.Variable([1,2,3,4])
a
 
#Get Variable Name, Shape, Data Type & convert into NumpyArray
a.name
 
a.shape
 
a.dtype
 
a.numpy()
 
type(a)
 
# # Create TF using Integer, Float, String, Bool, Complex Number
t_f = tf.Variable([1.2,4.4,5,6])
t_f
 
t_s = tf.Variable(['a','b','c','d'])
t_s
 
t_b = tf.Variable([True, False])
t_b
 
t_cx = tf.Variable([3 + 4j])
t_cx
 
# # Create TF from Constant TensorFlow Variable
t_con = tf.constant([1,2,3,4])
t_con
 
tf.Variable(t_con)
 
#  # Create TF Variable with different shape
t_2d = tf.Variable([[2,3], [4,5]])
t_2d
 
t_2d_2 = tf.Variable([[2,3], [4,5]], shape=(2,2), dtype='float32')
t_2d_2
 
a
 
tf.reshape(a, (2,2))
 
# # Get Index of highest value
t_2d_2
 
tf.argmax(t_2d_2)
 
tf.argmax(t_2d_2).numpy()
 
# # Viewed/convert as a tensor
a
 
tf.convert_to_tensor(a)
 
tf.convert_to_tensor(t_2d_2)
 
# # Change/Assign new value to tensor
a
 
a.assign([4,6,2,8])
a
 
# # Assign Variable with anothe memory
"""
If you use a variable like a tensor in operations, you will usually operate on the backing tensor.
 
Creating new variables from existing variables duplicates the backing tensors. Two variables will not share the same memory.
"""
a.assign_add([4,6,2,8])
 
# # Can't change shape and Data Type
a.assign([4,6,2,8,7])
 
a.assign([4.2,6.7,2.0,8.1])
