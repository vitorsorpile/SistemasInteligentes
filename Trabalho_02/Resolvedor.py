from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State
from spade.template import Template
from spade.message import Message
import random
import time

from main import email_resolvedor, senha_resolvedor, email_gerador

INITIAL_STATE = 'INITIAL_STATE'
CALCULATE_STATE = 'CALCULATE_STATE'
ANSWER_STATE = 'ANSWER_STATE'
SOLVE_FIRST_GRADE_STATE = 'SOLVE_FIRST_GRADE_STATE'
SOLVE_BY_BISECTION_STATE = 'SOLVE_BY_BISECTION_STATE'

class Resolvedor(Agent):

   class FSMBehaviour(FSMBehaviour):
      async def on_start(self):
         print(f"FSM starting at initial state {self.current_state}")
         

      async def on_end(self):
         print(f"FSM finished at state {self.current_state}")
         await self.agent.stop()


   class InitialState(State):
      async def run(self):
         print("I'm at the initial state")
         msg = Message(to=email_gerador)
         msg.set_metadata('performative', 'request')
         
         await self.send(msg)
         timeoutCounter = 0

         res = await self.receive(timeout=5)

         while not res:
            res = await self.receive(timeout=5)
            timeoutCounter += 1
            if (timeoutCounter >= 5):
               print('Parando agente após não ser respondido...')
               await self.agent.stop()

         print(f'Tenho que resolver uma equacao do tipo {res.body}')
         self.agent.tipoDaFuncao = res.body

         if (res.body == '1grau'):
            self.set_next_state(SOLVE_FIRST_GRADE_STATE)

         if (res.body == '2grau' or res.body == '3grau'):
            self.set_next_state(SOLVE_BY_BISECTION_STATE)
         
         else:
            self.set_next_state(CALCULATE_STATE)


   class AnswerState(State):
      async def run(self):
         msg = self.agent.msg

         print(f'Sending {msg.body} to {msg.to}')
         await self.send(msg)

         timeoutCounter = 0

         res = None
         res = await self.receive(timeout=5)

         while not res:
            res = await self.receive(timeout=5)
            timeoutCounter += 1
            if (timeoutCounter >= 5):
               print('Parando agente após não ser respondido...')
               await self.agent.stop()
         
    
         if res.body == '0':
            print(f'Found solution: {msg.body}')
            await self.agent.stop()

         if self.agent.tipoDaFuncao == '1grau':
            self.agent.coeficientes.append(int(res.body))
            self.set_next_state(SOLVE_FIRST_GRADE_STATE)

         if self.agent.tipoDaFuncao == '2grau' or self.agent.tipoDaFuncao == '3grau':
            if (int(res.body) > 0): self.agent.upper = int(res.body)
            else: self.agent.lower = int(res.body)
            self.set_next_state(SOLVE_BY_BISECTION_STATE)


   class SolveFirstGradeEquationState(State):
      async def run(self):
         if len(self.agent.coeficientes) == 0:
            self.agent.msg.body = '0'
            self.set_next_state(ANSWER_STATE)
            return

         if len(self.agent.coeficientes) == 1:
            self.agent.msg.body = '1'
            self.set_next_state(ANSWER_STATE)
            return
         
         # Caso o valor retornado na terceira execução não seja zero => não foi possível encontrar a solução
         if len(self.agent.coeficientes) > 2:
            print('Ihh, alguma coisa deu errado. Não foi possível encontrar uma solução.')
            await self.agent.stop()

         b = int(self.agent.coeficientes[0])

         a = int(self.agent.coeficientes[1]) - b
         print(f'a: {a}')
      
         x = int(-b/a)
         print(f'x: {x}')

         self.agent.msg.body = str(x)
         self.set_next_state(ANSWER_STATE)

   class SolveByBisection(State):
      async def run(self):
         m = (self.agent.upper + self.agent.lower)/2
         estimate = int(m)
         self.agent.msg.body = str(estimate)
         self.set_next_state(ANSWER_STATE)

   class CalculateState(State):
      async def run(self):
         msg = Message(to=email_gerador)
         msg.set_metadata('performative', 'subscribe')

         
         while(True):
            msg.body = str(random.randint(-1000, 1000))
            print(f'Sending {msg.body} to {msg.to}')
            await self.send(msg)

            res = await self.receive(timeout=5)
            if res.body == '0':
               print(f'Found solution: {msg.body}')
               await self.agent.stop()


   async def setup(self):
      self.coeficientes = []
      self.upper = 1000
      self.lower = -1000

      self.msg = Message(to=email_gerador)
      self.msg.set_metadata('performative', 'subscribe')

      stateMachine = FSMBehaviour()
      stateMachine.add_state(name=INITIAL_STATE, state=self.InitialState(), initial=True)
      stateMachine.add_state(name=SOLVE_FIRST_GRADE_STATE, state=self.SolveFirstGradeEquationState())
      stateMachine.add_state(name=SOLVE_BY_BISECTION_STATE, state=self.SolveByBisection())
      stateMachine.add_state(name=CALCULATE_STATE, state=self.CalculateState())
      stateMachine.add_state(name=ANSWER_STATE, state=self.AnswerState())
      stateMachine.add_transition(source=INITIAL_STATE, dest=SOLVE_FIRST_GRADE_STATE)
      stateMachine.add_transition(source=INITIAL_STATE, dest=SOLVE_BY_BISECTION_STATE)
      stateMachine.add_transition(source=INITIAL_STATE, dest=CALCULATE_STATE)
      stateMachine.add_transition(source=SOLVE_FIRST_GRADE_STATE, dest=ANSWER_STATE)
      stateMachine.add_transition(source=SOLVE_BY_BISECTION_STATE, dest=ANSWER_STATE)
      stateMachine.add_transition(source=ANSWER_STATE, dest=SOLVE_FIRST_GRADE_STATE)

      t = Template()
      t.set_metadata("performative","inform")

      self.add_behaviour(stateMachine, t)


[-369, 992, 886]

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