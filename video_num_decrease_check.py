# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 14:23:34 2018

@author: fangyucheng
"""

import pandas as pd
#from daily_utils import trans_format

work_file42 = 'F:/video_num_decrease_check/week42.csv'
work_file43 = 'F:/video_num_decrease_check/week43.csv'
work_file44 = 'F:/video_num_decrease_check/week44.csv'

df42 = pd.read_csv(work_file42, encoding='gb18030')
df43 = pd.read_csv(work_file43, encoding='gb18030')
df44 = pd.read_csv(work_file44, encoding='gb18030')
df42['count'] = 1
df43['count'] = 1
df44['count'] = 1
total_video42 = df42.groupby(by='releaser').sum()
total_video43 = df43.groupby(by='releaser').sum()
total_video44 = df44.groupby(by='releaser').sum()  

