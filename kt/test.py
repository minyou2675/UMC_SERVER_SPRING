import dog_breed_classification
import s3
import os
import torch
import pandas as pd
import glob
import cv2
import pymysql
import csv
import dog_breed_classification

# detection = torch.hub.load('./detection','custom', './detection/normal.pt', source='local')
# images = glob.glob('./개고양이/*.jpg')

# results = detection(images)
# results.save()
# crops = results.crop(save=True)

# path = './output/2.background_remove/'
# file_list = os.listdir('./output/2.background_remove')

# for file in file_list : 
#     replaced = file.replace('.png','.jpg')
#     os.rename(path+file,path+replaced)
