# class Animal:
#     def speak(self):
#         return "..."
# class Dog(Animal):
#     def speak(self):
#         return "wof"
# class Cat(Animal):
#     def speak(self):
#         return "meow"
    
# class Robot:         #Python’s special version: duck typing
#     def speak(self): #using polymorphism without inheritance or intereface
#         return "Beepboob"
# animals = [Dog(),Cat(),Robot()]

# for a in animals:
#     print (a.speak())
    
from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self,name):
        self.name = name
        self.__task_done = 0

    @abstractmethod
    def run(self,task):
        pass
    
    def _count(self):
        self.__task_done += 1
        
    @property
    def task_done(self):
        return self.__task_done
class ResearchAgent(Agent):
    def run(self,task):
        print(f"{self.name} is doing research on {task}")
        self._count()
        
class CodingAgent(Agent):
    def run(self,task):
        self._count()
        print(f"{self.name} is coding {task}")
       
agents = [ResearchAgent("Alice"),CodingAgent("Nova")]

for a in agents:
    a.run("AI")
    print(f"{a.name} has completed {a.task_done} tasks.")