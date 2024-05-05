import tensorflow as tf
import numpy as np

class RBM:
    def __init__(self, num_visible, num_hidden):
        self.num_visible = num_visible
        self.num_hidden = num_hidden
        self.weights = tf.Variable(tf.random.normal([num_visible, num_hidden], mean=0.0, stddev=0.01))
        self.bias_visible = tf.Variable(tf.zeros([num_visible]))
        self.bias_hidden = tf.Variable(tf.zeros([num_hidden]))

    def sample_hidden(self, visible_probabilities):
        hidden_activations = tf.nn.sigmoid(tf.matmul(visible_probabilities, self.weights) + self.bias_hidden)
        hidden_samples = tf.where(tf.random.uniform(shape=tf.shape(hidden_activations)) < hidden_activations, 1.0, 0.0)
        return hidden_samples

    def sample_visible(self, hidden_probabilities):
        visible_activations = tf.nn.sigmoid(tf.matmul(hidden_probabilities, tf.transpose(self.weights)) + self.bias_visible)
        visible_samples = tf.where(tf.random.uniform(shape=tf.shape(visible_activations)) < visible_activations, 1.0, 0.0)
        return visible_samples

    def free_energy(self, visible):
        energy = -tf.matmul(visible, tf.transpose(self.bias_visible))
        energy -= tf.reduce_sum(tf.math.log(1 + tf.exp(tf.matmul(visible, self.weights) + self.bias_hidden)), axis=1)
        return tf.reduce_mean(energy)

# Creación de una RBM con 5 neuronas visibles y 3 neuronas ocultas
rbm = RBM(5, 3)

# Generación de un lote de datos de entrada
batch_size = 10
datos_entrada = tf.random.uniform([batch_size, 5])

# Muestreo de la capa oculta
capa_oculta = rbm.sample_hidden(datos_entrada)

# Muestreo de la capa visible reconstruida
capa_visible_reconstruida = rbm.sample_visible(capa_oculta)

# Cálculo de la energía libre del sistema
energia_libre = rbm.free_energy(datos_entrada)
print("Energia libre del sistema:", energia_libre.numpy())
