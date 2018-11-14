# !/usr/bin/python
import os
import csv

cwd = os.getcwd()

pre_example_path = cwd+ "/data/Example Data/Pre_Example/"
post_example_path = cwd + "/data/Example Data/Post_Example/"

PRE_DATA = {}

for root, dirs, files in os.walk(pre_example_path):
    for file in files:
        with open(pre_example_path+file,"r+") as csvfile:
            reader = csv.reader(csvfile)
            PRE_DATA.update({file:reader})
            
