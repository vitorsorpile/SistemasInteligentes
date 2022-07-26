from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
import data_processing
import numpy as np
import matplotlib.pyplot as plt

class ModelBase():
    def __init__(self, model_topology):
        self.topology = model_topology
        if model_topology == 1:
            self.model = Sequential([
                Dense(units=100, input_shape= (1,), activation='relu'),
                Dense(units=100, activation='relu'),
                Dense(units=1)
            ])
        elif model_topology == 2:
            self.model = Sequential([
                Dense(units=45, input_shape= (1,), activation='elu'),
                Dense(units=30, activation='relu'),
                Dense(units=35, activation='tanh'),
                Dense(units=40, activation='relu'),
                Dense(units=1)
            ])
        elif model_topology == 3:
            self.model = Sequential([
                Dense(units=3000, input_shape= (1,), activation='relu'),
                Dense(units=1)
            ])
        else: print('Modelo selecionado inválido!')

    def compile_and_train(self, optm, lss, mtcs, samples, labels, val_splt, epcs, btch_sz, verb):
        self.model.compile(optimizer= optm,loss=lss, metrics=mtcs)
        self.hist = self.model.fit(x=samples, 
                                   y=labels, 
                                   validation_split=val_splt, 
                                   epochs=epcs, 
                                   batch_size=btch_sz, 
                                   verbose=verb)
    
    def compare_real_predicted(self, samples, labels):
        scaled_samples, scaled_labels, sc_shuf_samples, sc_shuf_labels = data_processing.normalize_and_shuffle(samples, labels)
        predictions = self.model.predict(x=scaled_samples, verbose=0)
        predictions = np.array(predictions)

        plt.title(f'Modelo {self.topology} - Real x Previsto')
        plt.plot(samples,labels,label='Valor Real')
        plt.plot(samples,predictions*max(labels), color='red',label='Valor da RNA')
        plt.legend(loc='upper left')
        plt.yticks([y for y in range(0, 1001, 100)])
        plt.xticks([x for x in range(1, 62, 4)])

        plt.show()

    def get_loss_graph(self):
        plt.title(f'Modelo {self.topology} - Perdas x Epoca')
        plt.plot(self.hist.history['loss'], label='Perdas')
        plt.legend(loc='upper left')
        plt.show()

    def save(self):
      self.model.save(f'model{self.topology}')