
from keras.preprocessing import sequence
from keras.layers.embeddings import Embedding
from keras.layers.convolutional import MaxPooling1D
from keras.layers.convolutional import Conv1D
from keras.layers import LSTM
from keras.layers import Dense
from keras.models import Sequential
from keras.datasets import imdb
import numpy
import os
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import tensorflow as tf

gpu = tf.config.experimental.list_physical_devices('GPU')
try:
    # Currently, memory growth needs to be the same across GPUs
    tf.config.experimental.set_memory_growth(gpu[0], True)
    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
except RuntimeError as e:
    # Memory growth must be set before GPUs have been initialized
    print(e)


# LSTM and CNN for sequence classification in the IMDB dataset
# fix random seed for reproducibility
numpy.random.seed(7)
# load the dataset but only keep the top n words, zero the rest
top_words = 5000
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)
# truncate and pad input sequences
max_review_length = 500
print(y_train)
# X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
# X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)
# # create the model
# embedding_vecor_length = 32
# model = Sequential()
# model.add(Embedding(top_words, embedding_vecor_length,
#                     input_length=max_review_length))
# model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
# model.add(MaxPooling1D(pool_size=2))
# model.add(LSTM(100))
# model.add(Dense(1, activation='sigmoid'))
# model.compile(loss='binary_crossentropy',
#               optimizer='adam', metrics=['accuracy'])
# print(model.summary())
# model.fit(X_train, y_train, epochs=3, batch_size=256)
# # Final evaluation of the modelvvvvvvvvv
# scores = model.evaluate(X_test, y_test, verbose=0)
# print("Accuracy: %.2f%%" % (scores[1]*100))
# model.save('./model.h5')
