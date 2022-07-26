from keras.optimizers import Adam
import data_processing
import warnings
import my_models
import sys

warnings.filterwarnings("ignore")

samples, labels = data_processing.get_data('dadosTrabalhoRNA.xlsx')

scaled_samples, scaled_labels, sc_shuf_samples, sc_shuf_labels = data_processing.normalize_and_shuffle(samples, labels)

if len(sys.argv) > 1:
   model = my_models.ModelBase(int(sys.argv[1]))

   model.compile_and_train(optm= Adam(learning_rate=0.0001), 
                           lss= 'mse', 
                           mtcs= ['mse'], 
                           samples= sc_shuf_samples, 
                           labels= sc_shuf_labels, 
                           val_splt= 0.15, 
                           epcs= 800, 
                           btch_sz= 3, 
                           verb= 2)

   model.compare_real_predicted(samples, labels)
   model.get_loss_graph()
   model.save()

else:
   for i in range(1,4):
      model = my_models.ModelBase(i)
      
      model.compile_and_train(Adam(learning_rate=0.0001), 'mse', ['mse'], sc_shuf_samples, sc_shuf_labels, 0.15, 800, 3, 2)
      model.compare_real_predicted(samples, labels)
      model.get_loss_graph()
      model.save()
