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
import matplotlib.pyplot as plt
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

    def exchange(self):
        # only exchange if weath is >0
        if self.wealth > 0:
            # random is same as python random but shares model seed so use it!
            other_agent = self.random.choice(self.model.agents)
            if other_agent is not None:
                other_agent.wealth += 1
                self.wealth -= 1


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
        self.agents.shuffle_do("exchange") #changing this to just 'do' makes agents ordered
    
    def run_for(self, steps):
        for _ in range(steps):
            self.step()


# --------Agents do--------------
# Mesa’s do function calls agent functions to grow your ABM. 
# A step is the smallest unit of time in the model, and is often referred to as a tick.

# --------Running model ---------
# The model can be run by creating a model object and calling the step method. 
# The model will run for one step and print the unique_id of each agent. 
# You may run the model for multiple steps by calling the step method multiple times.

# starter_model = MoneyModel(12) # Changing seed to number makes shuffle same order!
# starter_model.step()

# model = MoneyModel(10)  # Tells the model to create 10 agents
# for _ in range(30):  # Runs the model for 30 steps;
#     model.step()

# Note: An underscore is common convention for a variable that is not used.

# -------Getting and displaying the data --------

# agent_wealth = [a.wealth for a in model.agents]
# print(agent_wealth)
# Seaborn histogram
# g = sns.histplot(agent_wealth, discrete=True)
# g.set(title="Wealth distribution", xlabel="Wealth", ylabel="number of agents");  # The semicolon is just to avoid printing the object representation

# fixes ticks cuz of calling plt/ don't need this if run from jupyter
# min_w = min(agent_wealth)
# max_w = max(agent_wealth)
# g.set_xticks(range(min_w, max_w + 1))

# plt.show()


# Even better is to run multiple models and see emergin distribution

all_wealth = []

for _ in range(100):
    model = MoneyModel(100)
    model.run_for(30)

    # store results
    for agent in model.agents:
        all_wealth.append(agent.wealth)

g = sns.histplot(all_wealth, discrete=True)
g.set(title="Wealth distribution", xlabel="Wealth", ylabel="number of agents");
# fixes ticks cuz of calling plt/ don't need this if run from jupyter
min_w = min(all_wealth)
max_w = max(all_wealth)
g.set_xticks(range(min_w, max_w + 1))

plt.show()