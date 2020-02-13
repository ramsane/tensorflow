import tensorflow_core.python as tf
from tensorflow_core.python.keras.api._v2 import keras

(train_images, train_labels), (test_images, test_labels) = \
    keras.datasets.cifar10.load_data()
