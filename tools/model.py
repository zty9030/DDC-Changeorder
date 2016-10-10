# -*- coding: utf-8 -*-
import pickle
import pandas as pd
import numpy as np
import sklearn 

#x = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1094.0,8836540.0]
#x=np.array(x)
#result = modelrf.predict_proba(x)
#
#print result[0]

def randomforest(dic):
    
    modelrf = pickle.load(open('tools/modelrf.pickle','rb'))

    col = [u'Bronx & N. Queens', u'Brooklyn', u'Corrections', u'Courts',
       u'Culturals', u'Executive', u'Fire', u'Health', u'Human Services',
       u'Libraries', u'Manhattan & Citywide', u'Parks', u'Police',
       u'S. Queens', u'Sanitation', u'Staten Island', u'Transportation',
       u'CM Design Build', u'other', u'Pass-Through', u'Project Specific',
       u'Pure REI Manage', u'Regular', u'Regular Architecture & Engineering',
       u'Regular Design', u'Service Contracts', u'New Construction', u'Other',
       u'Ped Ramps', u'Renovation', u'Sewer', u'Sidewalks',
       u'Street Reconstruction', u'Street Resurfacing', u'Upgrade', u'Water',
       u'Cntrct_Duration', u'CntrctFeeAmt']

    pred = [1 if text in dic.values() else 0 for text in col]
    pred[-2]=dic['Duration'] 
    pred[-1] = dic['Amount']
    #print pred
    return [round(num,4) for num in modelrf.predict_proba([pred])[0]]


# li=['Bronx & N. Queens','Other','Sewer','100','10000']
# re = randomforest(li)
# print re




"""
Spyder Editor

This is a temporary script file.
"""

