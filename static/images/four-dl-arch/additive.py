import numpy as np
import tensorflow as tf
from tensorflow.keras import Input, Model
from tensorflow.keras.layers import Dense

units = 4

enc = np.random.rand(4, 16, 32).reshape(4, -1, 32).astype('float32')
dec = np.random.rand(4, 32).reshape(4, 1, 32).astype('float32')

enc_h = Input(shape=(None, 32))
dec_h = Input(shape=(1, 32))

w1 = Dense(units)(enc_h)
w2 = Dense(units)(dec_h)
v = Dense(1)

score = tf.nn.tanh(w1 + w2)
score = v(score)
attention = tf.nn.softmax(score, axis=1)
context = attention * enc_h
context = tf.reduce_sum(context, axis=1)

mdl = Model(inputs=[enc_h, dec_h], outputs=[score, attention, context])
score, attention, context = mdl([enc, dec])
print(f'score shape {score.shape}')
print(f'attention shape {score.shape}')
print(f'context shape {score.shape}')

enc = np.random.rand(4, 8, 32).reshape(4, -1, 32).astype('float32')
score, attention, context = mdl([enc, dec])
print(f'score shape {score.shape}')
print(f'attention shape {score.shape}')
print(f'context shape {score.shape}')
