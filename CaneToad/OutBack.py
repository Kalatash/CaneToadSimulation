# -*- coding: utf-8 -*-
import numpy as N

"""
Created on Mon May 11 20:04:32 2015

@author: Tim
"""

class OutBack:
    def __init__(self, dimensions, percent_toads=.80, food_init=.05, 
                 per_AWPs=.01, per_AWP_fence=.00):
        self.dimensions = dimensions
        self.percent_toads = percent_toads
        self.food_init = food_init
        self.per_AWPs = per_AWPs
        self.per_AWP_fence = per_AWP_fence
        
    def populate(self):
        self.hydro = N.zeros((self.dimensions[0]+2,self.dimensions[1]+2))
        self.food = N.zeros((self.dimensions[0]+2,self.dimensions[1]+2)) \
                  + self.food_init
        
