# file to practice mesa

# # Boltzmann Wealth Model tutorial
'''
The assumption that govern this model are:

- There are some number of agents.

- All agents begin with 1 unit of money.

- At every step of the model, an agent gives 1 unit of money (if they have it) to some other agent.
'''

import numpy as np
import pandas as np
import seaborn as sns
import mesa

# ------- Agent ----------------------------
# Agents have unique_id assigned at creation

class MoneyAgent(mesa.Agent):
    "Agent with fixed initial weath of 1 hryvna"

    def __init__(self, model):
        # Pass parameters to parent class
        super().__init__(model)
        # initial wealth value
        self.wealth = 1

    def say_hi(self):
        # Agent's step goes here

        print(f"Hi, I am an agent with id: {self.unique_id!s}. ")

    def say_wealth(self):
        print(f"Hi, my wealth is: {self.wealth}")


# ------ Model ----------------------------
# This is "manager" class that manages creation, activation, data collection etc. by agents
# very simply it's a list containing agents (in dictionary) with discrete time steps

class MoneyModel(mesa.Model):
    "Model with n number of agents"

    def __init__(self, n=10, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        # Create agents
        MoneyAgent.create_agents(model=self, n=n)
        # This is method from superclass Agent that handles creation of n agents with id assignment
        # it allso auto adds them to the model self.agents!

    def step(self):
        # Advances model by single step/tick
        # This function psuedo-randomly reorders the list of agent objects and
        # then iterates through calling the function passed in as the parameter
        self.agents.shuffle_do("say_wealth") #changing this to just 'do' makes agents ordered


# --------Agents do--------------
# Mesa’s do function calls agent functions to grow your ABM. 
# A step is the smallest unit of time in the model, and is often referred to as a tick.

# --------Running model ---------
# The model can be run by creating a model object and calling the step method. 
# The model will run for one step and print the unique_id of each agent. 
# You may run the model for multiple steps by calling the step method multiple times.

starter_model = MoneyModel(12) # Changing seed to number makes shuffle same order!
starter_model.step()


