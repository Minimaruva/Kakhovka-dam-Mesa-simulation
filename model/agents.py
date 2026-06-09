# People agents file

'''
Kakhovka dam disaster:
Using daat from :
Assumptions:
    1. Agents have mobility level 0-1 (float)
    2. Resources (abstracts water+food etc.) 0-1 float
    3. Flood zone 1-3 (how quickly water reaches them after dam blew up)
    4. Status: 
        - safe
        - displaced
        - at_risk

'''


import numpy as np
import pandas as pd
import mesa


class RefugeeAgent(mesa.Agent):
    
    def __ini__(self, model):
        super().__init__(model)

        self.status = "safe" # all agents start as safe
        
        # TODO: make proprotion of mobile agents skewed towards one end of mobility spectrum
        # TODO: check if this random initialisations should happen within model rather than agent class (for seed sake)
        self.mobility = self.random.random() # random mobility level between 0 and 1
        self.resources = self.random.random() # random resources level between 0 and 1 - skew towards higher?
        self.flood_zone = self.random.randint(1, 4) # random flood zone between 1 and 3
    
    def consume_resources(self):
        # simple resource consumption logic - can be made more complex
        if self.status == "at_risk":
            self.resources += 0.1 # start gather resources?
        elif self.status == "displaced":
            self.resources -= 0.15 # no access to resource
        else:
            self.resources += 0 # no need to oversave when safe

        # Ensure resources don't go negative
        self.resources = max(self.resources, 0)


