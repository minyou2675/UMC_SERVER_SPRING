import matplotlib.pyplot as plt

import tensorflow as tf
from keras.models import Sequential
from keras.applications.imagenet_utils import decode_predictions

from keras.applications.efficientnet_v2 import EfficientNetV2L
# from keras.applications.resnet50 import preprocess_input
import cv2
import os
import csv
import numpy as np
import PIL.Image as pil
import pandas as pd
import numpy as np
import glob



class models():
  def __init__(self):
    self.model = EfficientNetV2L(include_top=True,input_shape= (480,480,3),weights = 'imagenet')
    self.k = 0
    self.df = pd.DataFrame(columns=['filename',1,2,3])

  def pred_img(self,img_path):
    img = pil.open(img_path)
    plt.imshow(img)
    plt.axis('off')
    
    plt.show
  
    img_resized = img.resize((480,480))
    img_resized = np.array(img_resized)
    pred = self.model.predict(img_resized.reshape(([1, 480, 480, 3])))
    decoded_pred = decode_predictions(pred)
    img_path_name = os.path.basename(img_path)
   

    self.df.loc[self.k,'filename'] = f"{img_path_name}"
    
    for i, instance in enumerate (decoded_pred[0]):
      # print('{}위:{}({:.2f}%)'.format(i+1,instance[1],instance[2]*100))
      self.df.loc[self.k,i+1] = str(instance[1])+'('+str(int(instance[2]*100))+'%)' 
      # os.makedirs('./csv',exist_ok=True)
      # f = open('write.csv','w',newline='')
      # wr = csv.writer(f)
      # wr.writerow([instance[1],instance[2]*100])

      if i == 2 : break
    self.k += 1

    #예측 결과를 데이터프레임으로 output
  def export(self,image_path):
    files = glob.glob(f'{image_path}/*.jpg')
    for f in files:
      self.pred_img(f)
      print(f)
  
    print(self.df)
    self.df.to_csv("./breed2.csv")
    return self.df

    