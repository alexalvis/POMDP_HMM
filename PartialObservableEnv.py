# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 22:40:25 2022

@author: 53055
"""

import numpy as np
import MDP

class PartialObs(MDP):
    def __init__(self, MDP, Statetype, ObsPro, Obslist):
        self.MDP = MDP
        self.statetype = Statetype  #dictionary, key: state, value: sensor type
        self.ObsPro = ObsPro   #dictionary, key: sensortype, value: Probability list
        self.Obslist = Obslist  #list: observation list
    
    def observation(self, state):
        if state in self.statetype.keys():
            sensortype = self.statetype[state]
        else:
            return "epsilon"
        probability = self.ObsPro[sensortype]
        cho = np.random.choice(len(probability), 1, p = probability)[0]
        return self.Obslist[cho]
    
    def st_obs_Mat(self):
        statelen = len(self.MDP.statespace)
        obslen = len(self.Obslist)
        st_obs_mat = np.zeros((statelen, obslen))
        for i in range(statelen):
            sensortype = self.statetype[self.MDP.statespace[i]]
            pro = self.ObsPro[sensortype]
            for j in range(obslen):
                st_obs_mat[i][j] = pro[j]
        return st_obs_mat

def Forward(sttrans, stobs, init, traj):
    alpha = np.zeros((traj.shape[0], sttrans.shape[0]))
    alpha[0, :] = init * stobs[:, traj[0]]  #traj[0] should correspond to the observation index, instead of true observation
    #init * stobs, elementwise multiply alpha[0][i] time step 0, probability of state[i] when receiving observation traj[0]
    for t in range(1, traj.shape[0]):
        for j in range(sttrans.shape[0]):
            alpha[t, j] = alpha[t-1].dot(sttrans[:, j]) * stobs[j, traj[t]]
    #alpha[t-1].dot(sttrans[:, j]) from last time step, the probability to state j
    #For different trajectory, we need to calculate different alpha
    return alpha 