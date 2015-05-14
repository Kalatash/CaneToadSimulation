# -*- coding: utf-8 -*-
#import numpy as N

"""
Toads to use in Cane Toad Simulation

@author: Tim
"""

class Toad:
    def __init__(self, starting_range=.12, may_hop=.5, 
                 water_hopping=.002, energy_hopping=.002,  
                 desiccate=.6, starve=.6, 
                 would_like_drink=.9, would_like_eat=.9):
        self.may_hop = may_hop
        self.water_hopping = water_hopping
        self.energy_hopping = energy_hopping
        self.desiccate = desiccate
        self.starve = starve
        self.would_like_drink = would_like_drink
        self.would_like_eat = would_like_eat
        