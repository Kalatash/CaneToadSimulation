# -*- coding: utf-8 -*-
import numpy as N
import Frog

"""
Cane Toad Simulation

@author: Tim
"""

class OutBack:
    def __init__(self, dimensions, uber_toad=Frog, percent_toads=.80, food_init=.05, 
                 per_AWPs=.01, per_AWP_fence=.00):
        self.dimensions = dimensions
        self.percent_toads = percent_toads
        self.food_init = food_init
        self.per_AWPs = per_AWPs
        self.per_AWP_fence = per_AWP_fence
        self.uber_toad = uber_toad
        self.toads = []
        self.live_toads = 0
        self.dead_toads = 0
        
    def initulize(self):
        exp_dim = (self.dimensions[0]+2, self.dimensions[1]+2)
        self.hydro = N.zeros(exp_dim) - 1
        self.food = N.zeros(exp_dim) - 1
        self.barrier = N.zeros(exp_dim, dtype=bool)
        
        self.hydro[:,0] = 2
        self.hydro[1:-1,1:-1] = 0
        self.food[:,0] = 2
        self.food[1:-1,1:-1] = self.food_init
        self.barrier[0,:] = True
        self.barrier[0,:] = True