from tensorflow import keras
from keras.optimizers import Adam
import data_processing
import warnings
import my_models
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

samples, labels = data_processing.get_data('dadosTrabalhoRNA.xlsx')

scaled_samples, scaled_labels, sc_shuf_samples, sc_shuf_labels = data_processing.normalize_and_shuffle(samples, labels)

model1 = my_models.ModelBase(1)
model2 = my_models.ModelBase(2)
model3 = my_models.ModelBase(3)

#model1.model.summary()

model1.compile_and_train(Adam(learning_rate=0.0001), 'mse', ['mse'], sc_shuf_samples, sc_shuf_labels, 0.15, 600, 3, 2)
model1.compare_real_predicted(samples, labels)
model1.get_loss_graph()

model1.predict_input(samples,labels)