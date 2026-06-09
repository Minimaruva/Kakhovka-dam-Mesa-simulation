# Disaster model file

'''
Kakhovka dam disaster:
Using daat from :
Assumptions:
    1.
    2.
    3.

'''


import numpy as np
import pandas as pd
import mesa
from agents import RefugeeAgent

class FloodModel(mesa.Model):
    def __init__(self, n=10, seed=None):
        super().__init__()
        self.num_agents = n
        RefugeeAgent.create_agents(model=self, n=n)


    def step(self):
        self.agents.shuffle_do("_")
    
    def run_for(self, steps):
        for _ in range(steps):
            self.step()


