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


# ------ Model ----------------------------
# This is "manager" class that manages creation, activation, data collection etc. by agents
# very simply it's a list containing agents (in dictionary) with discrete time steps

class MoneyModle(mesa.Model):
    "Model with n number of agents"

    def __init__(self, n=10, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        # Create agents
        MoneyAgent.create_agents(model=self, n=n)
        # This is method from superclass Agent that handles creation of n agents with id assignment
        # it allso auto adds them to the model self.agents!