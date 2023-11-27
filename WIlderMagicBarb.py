# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:30:03 2020
WMB Effects 
@author: Cameron Manis
"""

import numpy.random as nprand
import numpy as np
import os
import pandas

path = '...'
os.chdir(path)
filename1 = 'BARBARIAN.csv'

#from dataclasses import dataclass
#
#@dataclass
#class Xcondition:
#    a:int = 3
#    x:float = 0.
#    y:float = 0.
#X = Xcondition()
#print(X.x)


class Condition(object):
    def __init__(self,effect,active=False):
        self.effect = effect
        self.active= active
        
data = pandas.read_csv(filename1)
        
effects = {k: None for k in data.columns}


for k, v in effects.items():
    effects[k] = Condition(data[k].dropna().to_numpy(dtype=str))
effects['Generic'].active= True

"""
Emotional state
"""
effects['Confident'].active= True
effects['Brave'].active= True
#effects['Powerful'].active= True
#effects['Protective'].active= True
effects['Conflicted'].active= True
#effects['Afraid'].active= True
#effects['Vulnerable'].active= True
#effects['Impotent'].active= True
#effects['Envious'].active= True

"""
Around Magic    WIP
"""
#effects['Around magic'].active= True

"""
Recent Damage
"""
#effects['Fire'].active= True
#effects['Cold'].active= True
#effects['Necrotic'].active= True
#effects['Radiant'].active= True
#effects['Thunder'].active= True
#effects['Lightning'].active= True
#effects['Force'].active= True
#effects['Psychic'].active= True
#effects['Poison'].active= True
#effects['Acid'].active= True

"""
Boss Fight
"""

effects['Boss fight only:'].active= True


"""
Demonic
"""
effects['Demonic'].active= True

"""
Effect Randomizer
"""

Effect = np.array([])

def AddEff(cond,total):
    if cond.active:
        eff = cond.effect[nprand.randint(0,cond.effect.size)]
        total = np.append(total,eff)
        """
        total = np.append(total,cond.effect)
        """
    return total
    
for k,v in effects.items():
    if effects[k].active:
        Effect =AddEff(v,Effect)


Roll = nprand.randint(0,Effect.size)
    
print(Effect[Roll])
