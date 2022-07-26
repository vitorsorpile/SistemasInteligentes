import sys, os, warnings
from keras.models import load_model
from colorama import Fore, Style
import data_processing

warnings.filterwarnings("ignore")

model = None

if len(sys.argv) > 1:
   model_path = f'model{sys.argv[1]}'
   if os.path.exists(model_path):
      model = load_model(model_path)
   else:
      print(f'\nRNA {model_path} não foi encontrada. Tente treiná-la primeiro por meio do arquivo \"main.py\".')
      exit()

samples, labels = data_processing.get_data('dadosTrabalhoRNA.xlsx')

read_value = float(input('Insira um valor dentro do intervalo de treinamento (0 a 60): '))

while(read_value < 0 or read_value > 60):
    print(Fore.RED + '\nVALOR FORA DO INTERVALO!\n')
    print(Style.RESET_ALL)
    read_value = int(input('Insira um valor dentro do intervalo de treinamento (0 a 60): '))

while(read_value >= 0 and read_value <= 60):
    prediction = model.predict([read_value/max(samples)],verbose=0)
    print('\nO valor previsto pela RNA foi: '+str(round(prediction[0][0]*max(labels),2))+'\n')
    read_value = float(input('Insira um valor dentro do intervalo de treinamento ou fora para sair: '))