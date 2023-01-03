# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 13:54:52 2022

@author: 53055
"""

import numpy as np

def state_type_dict():
    state_type_d = {}
    state_type_d[(0, 0)] = "b"
    state_type_d[(0, 1)] = "b" 
    state_type_d[(0, 2)] = "b" 
    state_type_d[(1, 0)] = "b" 
    state_type_d[(1, 1)] = "b" 
    state_type_d[(1, 2)] = "b" 
    state_type_d[(1, 3)] = "b" 
    state_type_d[(2, 0)] = "b" 
    state_type_d[(2, 3)] = "b"
    state_type_d[(5, 1)] = "r"
    state_type_d[(5, 2)] = "r" 
    state_type_d[(5, 3)] = "r" 
    state_type_d[(5, 4)] = "r" 
    state_type_d[(5, 5)] = "r" 
    state_type_d[(4, 5)] = "r" 
    state_type_d[(3, 5)] = "r" 
    state_type_d[(2, 5)] = "r" 
    state_type_d[(0, 5)] = "r"
    state_type_d[(0, 3)] = "p"
    state_type_d[(0, 4)] = "p" 
    state_type_d[(1, 4)] = "p" 
    state_type_d[(2, 1)] = "p" 
    state_type_d[(2, 2)] = "p" 
    state_type_d[(2, 4)] = "p" 
    state_type_d[(3, 0)] = "p" 
    state_type_d[(3, 1)] = "p" 
    state_type_d[(3, 2)] = "p" 
    state_type_d[(3, 4)] = "p" 
    state_type_d[(4, 0)] = "p" 
    state_type_d[(4, 1)] = "p" 
    state_type_d[(4, 2)] = "p" 
    state_type_d[(4, 3)] = "p" 
    state_type_d[(4, 4)] = "p" 
    return state_type_d

def obs_type():
    obs_type_d = {}
    obs_type_d["b"] = [1/8, 7/8]
    obs_type_d["r"] = [7/8, 1/8]
    obs_type_d["p"] = [1/2, 1/2]
    return obs_type_d

def obs_list():
    return ["Low", "High"]
    