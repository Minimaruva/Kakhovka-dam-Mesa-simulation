# People agents file

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


class RefugeeAgent(mesa.Agent):
    
    def __ini__(self, model):
        super().__init__(model)
        self.alive = True # Assuming agents are alive at the start
    

