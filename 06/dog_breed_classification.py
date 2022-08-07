import matplotlib.pyplot as plt

import tensorflow as tf
from keras.models import Sequential
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras import datasets
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.applications.resnet50 import preprocess_input
import cv2
import os
import csv
import numpy as np
import PIL.Image as pil



class models():
  def __init__(self):
    self.model = VGG19(include_top=True,input_shape= (224,224,3),weights = 'imagenet')

  def pred_img(self,img_path):
    img = pil.open(img_path)
    plt.imshow(img)
    plt.axis('off')
    
    plt.show
    

    img_resized = img.resize((224,224))
    img_resized = np.array(img_resized)
    pred = self.model.predict(img_resized.reshape(([1, 224, 224, 3])))
    decoded_pred = decode_predictions(pred)
    
    for i, instance in enumerate (decoded_pred[0]):
      print('{}위:{}({:.2f}%)'.format(i+1,instance[1],instance[2]*100))
      os.makedirs('./csv',exist_ok=True)
      f = open('write.csv','w',newline='')
      wr = csv.writer(f)
      wr.writerow([instance[1]])

      if i == 2 : break

model = models()
model.pred_img('4.jfif')


    