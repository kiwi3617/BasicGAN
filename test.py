import tensorflow as tf

def inference():
    return None

def train():
    return None

def preprocess():
    return None

def image_read():
    return None

def generator():
    return None

def discriminator():
    return None

if __name__ == "__main__" :
    sess = tf.Session()

    input = tf.constant( [
        [
            [ [0.0], [1.0] , [2.0] , [3.0] , [4.0] , [5.0] ],
            [ [0.1], [1.1] , [2.1] , [3.1] , [4.1] , [5.1] ],
            [ [0.2], [1.2] , [2.2] , [3.2] , [4.2] , [5.2] ],
            [ [0.3], [1.3] , [2.3] , [3.3] , [4.3] , [5.3] ],
            [ [0.4], [1.4] , [2.4] , [3.4] , [4.4] , [5.4] ],
            [ [0.5], [1.5] , [2.5] , [3.5] , [4.5] , [5.5] ],
        ]
    ],dtype=tf.float32)

    kernel = tf.constant( [
        [ [[0.0]] , [[0.5]] , [[0.0]] ] ,
        [ [[0.0]] , [[1.0]] , [[0.0]] ] ,
        [ [[0.0]] , [[0.5]] , [[0.0]] ]
    ])

    #layer1 = tf.nn.conv2d(input,kernel,strides=[1,2,2,1], padding='SAME')
    features = tf.range(-2,2,0.5)
    f_array = sess.run(features)

    f_relu = tf.nn.relu(features)
    f_relu_out = sess.run(f_relu)

    f_sigmoid = tf.nn.sigmoid(features)
    f_sigmoid_out = sess.run(f_sigmoid)

    f_tanh = tf.nn.tanh(features)
    f_tanh_out = sess.run(f_tanh)

    print(f_array)
    print(f_relu_out)
    print(f_sigmoid_out)
    print(f_tanh_out)
