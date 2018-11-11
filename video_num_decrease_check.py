# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 14:23:34 2018

@author: fangyucheng
"""

import pandas as pd
#from daily_utils import trans_format

work_file42 = 'D:/python_code/database/week42.csv'
work_file43 = 'D:/python_code/database/week43.csv'

df42 = pd.read_csv(work_file42, encoding='gb18030')
df43 = pd.read_csv(work_file43, encoding='gb18030')
df42['count'] = 1
df43['count'] = 1
total_video42 = df42.groupby(by='releaser').sum()
total_video43 = df43.groupby(by='releaser').sum()  