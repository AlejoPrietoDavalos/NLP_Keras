from numpy import dtype
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.utils import to_categorical

mnist = tf.keras.datasets.mnist                             # Imágenes de Mnist 28x28.
(x_train, y_train),(x_test, y_test) = mnist.load_data()

x_train = x_train.astype(dtype="float32") / 255.0
x_test = x_test.astype(dtype="float32") / 255.0



#y_train = to_categorical(y_train)
#y_test = to_categorical(y_test)



#print(y_train.shape)
#print(y_test.shape)






model = Sequential()

# IF you are running with a GPU, try out the CuDNNLSTM layer type instead (don't pass an activation, tanh is required)
model.add(LSTM(128, input_shape=(x_train.shape[1:]), activation='relu', return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(128, activation='relu'))
model.add(Dropout(0.1))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(10, activation='softmax'))

opt = tf.keras.optimizers.Adam(lr=0.001, decay=1e-6)

# Compile model
model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer=opt,
    metrics=['accuracy'],
)

model.fit(x_train,
          y_train,
          epochs=3,
          validation_data=(x_test, y_test))