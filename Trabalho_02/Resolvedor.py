from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, FSMBehaviour, State
from spade.template import Template
from spade.message import Message
import random
import time

from main import email_resolvedor, senha_resolvedor, email_gerador

INITIAL_STATE = 'INITIAL_STATE'
ANSWER_STATE = 'ANSWER_STATE'
CALCULATE_STATE = 'CALCULATE_STATE'

class Resolvedor(Agent):

   class FSMBehaviour(FSMBehaviour):
      async def on_start(self):
         print(f"FSM starting at initial state {self.current_state}")
         

      async def on_end(self):
         print(f"FSM finished at state {self.current_state}")
         await self.agent.stop()


   class InitialState(State):
      async def run(self):
         print("I'm at state one (initial state)")
         msg = Message(to=email_gerador)
         msg.set_metadata('performative', 'request')
         await self.send(msg)

         res = await self.receive(timeout=5)
         if res:
            print(f'Tenho que resolver uma equacao do tipo {res.body}')
            # Set a first value to try to answer
            self.agent.answer = random.randint(-1000, 1000)
            self.set_next_state(ANSWER_STATE)

   class AnswerState(State):
      async def run(self):
         print("I'm at answer state ")

         msg = Message(to=email_gerador)
         msg.set_metadata('performative', 'subscribe')
         msg.body = str(self.agent.answer)
         await self.send(msg)

         msg = await self.receive(timeout=5)
         if msg.body == '0':
            print(f'Found solution!')
            await self.agent.stop()

         else:
            print('Essa nao era a solucao')
            self.set_next_state(CALCULATE_STATE)

   class CalculateState(State):
      async def run(self):
         self.agent.answer = random.randint(-1000, 1000)
         
         self.set_next_state(ANSWER_STATE)


   async def setup(self):
      stateMachine = FSMBehaviour()
      stateMachine.add_state(name=INITIAL_STATE, state=self.InitialState(), initial=True)
      stateMachine.add_state(name=ANSWER_STATE, state=self.AnswerState())
      stateMachine.add_state(name=CALCULATE_STATE, state=self.CalculateState())
      stateMachine.add_transition(source=INITIAL_STATE, dest=ANSWER_STATE)
      stateMachine.add_transition(source=ANSWER_STATE, dest=CALCULATE_STATE)
      stateMachine.add_transition(source=CALCULATE_STATE, dest=ANSWER_STATE)

      t = Template()
      t.set_metadata("performative","inform")

      self.add_behaviour(stateMachine, t)


#      tf = self.resposta()
 #     self.add_behaviour(tf,t)


resolvedor = Resolvedor(email_resolvedor, senha_resolvedor)
#resolvedor.web.start(hostname="127.0.0.1", port="10000")
future = resolvedor.start()
future.result()

while resolvedor.is_alive():
   try:
      time.sleep(1)

   except KeyboardInterrupt:
      resolvedor.stop()
      break