from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
import data_processing
import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore, Style

class ModelBase():
    def __init__(self, model_topology):
        if model_topology == 1:
            self.model = Sequential([
                Dense(units=256, input_shape= (1,), activation='relu'),
                Dense(units=128, activation='relu'),
                Dense(units=64, activation='relu'),
                Dense(units=32, activation='relu'),
                Dense(units=16, activation='relu'),
                Dense(units=8, activation='relu'),
                Dense(units=1)
            ])
        elif model_topology == 2:
            self.model = Sequential([
                Dense(units=256, input_shape= (1,), activation='elu'),
                Dense(units=128, activation='relu'),
                Dense(units=64, activation='tanh'),
                Dense(units=32, activation='tanh'),
                Dense(units=16, activation='relu'),
                Dense(units=8, activation='relu'),
                Dense(units=1)
            ])
        elif model_topology == 3:
            self.model = Sequential([
                Dense(units=128, input_shape= (1,), activation='relu'),
                Dense(units=128, activation='relu'),
                Dense(units=128, activation='relu'),
                Dense(units=128, activation='relu'),
                Dense(units=128, activation='relu'),
                Dense(units=128, activation='relu'),
                Dense(units=1)
            ])
        else: print('Modelo selecionado inválido!')

    def compile_and_train(self, optm, lss, mtcs, samples, labels, val_splt, epcs, btch_sz, verb):
        self.model.compile(optimizer= optm,loss=lss, metrics=mtcs)
        self.hist = self.model.fit(x=samples, y=labels, validation_split=val_splt, epochs=epcs, batch_size=btch_sz, verbose=verb)
    
    def compare_real_predicted(self, samples, labels):
        scaled_samples, scaled_labels, sc_shuf_samples, sc_shuf_labels = data_processing.normalize_and_shuffle(samples, labels)
        predictions = self.model.predict(x=scaled_samples, verbose=0)
        predictions = np.array(predictions)

        plt.title('Real x Previsto')
        plt.plot(samples,labels,label='Valor Real')
        plt.plot(samples,predictions*max(labels), color='red',label='Valor da RNA')
        plt.legend(loc='upper left')

        plt.show()    

    def get_loss_graph(self):
        plt.title('Perdas x Epoca')
        plt.plot(self.hist.history['loss'], label='Perdas')
        plt.legend(loc='upper left')
        plt.show()

    def predict_input(self,samples,labels):
        read_value = float(input('Insira um valor dentro do intervalo de treinamento (0 a 60): '))
        while(read_value < 0 or read_value > 60):
            print(Fore.RED + '\nVALOR FORA DO INTERVALO!\n')
            print(Style.RESET_ALL)
            read_value = int(input('Insira um valor dentro do intervalo de treinamento (0 a 60): '))
        while(read_value > 0 and read_value < 60):
            prediction = self.model.predict([read_value/max(samples)],verbose=0)
            print('\nO valor previsto pela RNA foi: '+str(round(prediction[0][0]*max(labels),2))+'\n')
            read_value = float(input('Insira um valor dentro do intervalo de treinamento ou fora para sair: '))