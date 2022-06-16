import time
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.template import Template
from spade.message import Message
from math import prod
import random

from main import email_gerador, senha_gerador

class Gerador(Agent):
   
   def gerarCoeficientes(self):
      self.raizes = []
      self.coeficientes = []

      for _ in range(self.grauDaFuncao):
         self.raizes.append(random.randint(-1000, 1000))
   
      print(self.raizes)
      a = random.randint(-10, 10)
      while (a == 0):
         a = random.randint(-10, 10)

      if self.grauDaFuncao == 1:
         self.coeficientes.append(-1 * a * self.raizes[0])

      else:
         soma = sum(self.raizes)
         produto = prod(self.raizes)

         if self.grauDaFuncao == 2:
            self.coeficientes.append(produto * a)
            self.coeficientes.append(-1 * soma * a)
         
         elif self.grauDaFuncao == 3:
            soma_dos_produtos = self.raizes[0] * self.raizes[1] + self.raizes[0] * self.raizes[2] + self.raizes[1] * self.raizes[2]

            self.coeficientes.append(-1 * produto * a)
            self.coeficientes.append(soma_dos_produtos * a)
            self.coeficientes.append(-1 * soma * a)
         
      self.coeficientes.append(a)

   def calcularResposta(self, x):
      resposta = 0
      i = 0
      for coeficiente in self.coeficientes:
         resposta += coeficiente*(x**i)
         i += 1

      return resposta

   class responderValor(CyclicBehaviour):
      async def run(self):
         res = await self.receive(timeout=5)
         if res:
               x = float(res.body)
               y = float(self.agent.calcularResposta(x))
               print("Enviou para " + str(res.sender) + " f(",res.body,")= ",y,"=>",int(y))
               msg = Message(to=str(res.sender)) 
               msg.set_metadata("performative", "inform")  
               msg.body = str(int(y))
               await self.send(msg)

   class tipo_funcao(CyclicBehaviour):
      async def run(self):
         msg = await self.receive(timeout=5)
         if msg:
               msg = Message(to=str(msg.sender))
               msg.set_metadata("performative", "inform")
               msg.body = f"{self.agent.grauDaFuncao}grau" 
               await self.send(msg)
               print("Respondeu para " + str(msg.sender) + " com " + msg.body)
               

   async def setup(self):
      self.grauDaFuncao = random.randint(1, 3)

      self.gerarCoeficientes()
      print(f'Equacao do {self.grauDaFuncao} grau')
      print(f'de coeficientes: {self.coeficientes}')
      self.x = random.randint(-1000, 1000)

      t = Template()
      t.set_metadata("performative","subscribe")

      tf = self.responderValor()
      # print("Funcao de 1o grau: ", Gerador.x)
      # print("Funcao: ", Gerador.a, "x + (", Gerador.y, ")")

      self.add_behaviour(tf,t)

      ft = self.tipo_funcao()
      template = Template()
      template.set_metadata("performative", "request")
      self.add_behaviour(ft, template)

gerador = Gerador(email_gerador, senha_gerador)
#gerador.web.start(hostname="127.0.0.1", port="10000")
future = gerador.start()
future.result()

while gerador.is_alive():
   try:
      time.sleep(1)

   except KeyboardInterrupt:
      gerador.stop()
      break