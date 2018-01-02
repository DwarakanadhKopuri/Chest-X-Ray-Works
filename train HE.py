# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import shutil
import os
import pandas as pd
os.chdir('F:/FD/Python/Hackerearth Chest')

train_csv = pd.read_csv('train.csv')
train_csv.shape
home_dir = 'F:/FD/Python/Hackerearth Chest/flow_from_directory/train/'
for index,row in train_csv.iterrows():
    if row[5] == 'class_1':
        dest_dir = home_dir+'class_1/'
        if not os.path.exists(dest_dir):
            os.makedirs(home_dir+'class_1')
        shutil.copy2('train/'+row[4], dest_dir+row[4])
    elif row[5] == 'class_2':
        dest_dir = home_dir+'class_2/'
        if not os.path.exists(dest_dir):
            os.makedirs(home_dir+'class_2')
        shutil.copy2('train/'+row[4], dest_dir+row[4])   
    elif row[5] == 'class_3':
        dest_dir = home_dir+'class_3/'
        if not os.path.exists(dest_dir):
            os.makedirs(home_dir+'class_3')
        shutil.copy2('train/'+row[4], dest_dir+row[4])  
    elif row[5] == 'class_4':
        dest_dir = home_dir+'class_4/'
        if not os.path.exists(dest_dir):
            os.makedirs(home_dir+'class_4')
        shutil.copy2('train/'+row[4], dest_dir+row[4])   
    elif row[5] == 'class_5':
        dest_dir = home_dir+'class_5/'
        if not os.path.exists(dest_dir):
            os.makedirs(home_dir+'class_5')
        shutil.copy2('train/'+row[4], dest_dir+row[4]) 
    elif row[5] == 'class_6':
        dest_dir = home_dir+'class_6/'
        if not os.path.exists(dest_dir):
            os.makedirs(home_dir+'class_6')
        shutil.copy2('train/'+row[4], dest_dir+row[4])   
    elif row[5] == 'class_7':
        dest_dir = home_dir+'class_7/'
        if not os.path.exists(dest_dir):
            os.makedirs(home_dir+'class_7')
        shutil.copy2('train/'+row[4], dest_dir+row[4])   
    elif row[5] == 'class_8':
        dest_dir = home_dir+'class_8/'
        if not os.path.exists(dest_dir):
            os.makedirs(home_dir+'class_8')
        shutil.copy2('train/'+row[4], dest_dir+row[4])   
    elif row[5] == 'class_9':
        dest_dir = home_dir+'class_9/'
        if not os.path.exists(dest_dir):
            os.makedirs(home_dir+'class_9')
        shutil.copy2('train/'+row[4], dest_dir+row[4])       
    elif row[5] == 'class_10':
        dest_dir = home_dir+'class_10/'
        if not os.path.exists(dest_dir):
            os.makedirs(home_dir+'class_10')
        shutil.copy2('train/'+row[4], dest_dir+row[4]) 
    elif row[5] == 'class_11':
        dest_dir = home_dir+'class_11/'
        if not os.path.exists(dest_dir):
            os.makedirs(home_dir+'class_11')
        shutil.copy2('train/'+row[4], dest_dir+row[4]) 
    elif row[5] == 'class_12':
        dest_dir = home_dir+'class_12/'
        if not os.path.exists(dest_dir):
            os.makedirs(home_dir+'class_12')
        shutil.copy2('train/'+row[4], dest_dir+row[4]) 
    elif row[5] == 'class_13':
        dest_dir = home_dir+'class_13/'
        if not os.path.exists(dest_dir):
            os.makedirs(home_dir+'class_13')
        shutil.copy2('train/'+row[4], dest_dir+row[4]) 
    elif row[5] == 'class_14':
        dest_dir = home_dir+'class_14/'
        if not os.path.exists(dest_dir):
            os.makedirs(home_dir+'class_14')
        shutil.copy2('train/'+row[4], dest_dir+row[4]) 
    
    else:
        print 'not this class'
        




