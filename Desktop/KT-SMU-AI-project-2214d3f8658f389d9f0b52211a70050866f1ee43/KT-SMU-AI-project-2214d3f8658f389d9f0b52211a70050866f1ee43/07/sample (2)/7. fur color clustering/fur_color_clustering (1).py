# -*- coding: utf-8 -*-
"""fur_color_clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xioplh3riJXKMnbi0HwiYN-8PYRLB_QH
"""

from google.colab import drive
drive.mount('/content/drive')

import os #chdir 사용시 필요함
import glob #파일 경로
import cv2
from google.colab.patches import cv2_imshow

images='/content/drive/MyDrive/sample (1)/3. background remove/1.jpg' #불러올 파일

#이미지 url 을open CV에 읽어들이기
image = cv2.imread(images)

from google.colab.patches import cv2_imshow

img = cv2.imread('/content/drive/MyDrive/sample (1)/3. background remove/1.jpg')
cv2_imshow(img)

# 잘 나온 이미지만을 가져오기 위해서 크롤러 대신 수작업을 선택해야 할지도 모르겠습니다.

#1. 클러스터링 (rgb)

import cv2 # 색상감지를 위한 opencv활용
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import scipy.misc

image_path = "/content/drive/MyDrive/sample (1)/3. background remove/1.jpg"
def image_color_cluster(image_path, k = 5):
    image = cv2.imread(image_path)
    # 3차원형태의 ndarray가 생성되었을것
    # 리턴 되는 숫자가 3개가 있어야 정상. return 되는 숫자의 의미는 (height, width, channel) /채널: rgb의 3채널
    
    # 주의해야할게 opencv로 이미지를 읽어들이면 RGB순서가 아닌 BGR값으로 리턴이 된다는 것
    # 채널을 BGR -> RGB로 변경
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = image.reshape((image.shape[0] * image.shape[1], 3))
    # shape의 0,1번째 즉, height와 width를 통합시킴

    print(image.shape)
     # (-, -) 숫자 두개로 나올 것

def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist
    
def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
    # of each of the colors
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    # loop over the percentage of each cluster and the color of
    # each cluster
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

def image_color_cluster(image_path, k = 5):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    
    clt = KMeans(n_clusters = k)
    clt.fit(image)

    hist = centroid_histogram(clt)
    bar = plot_colors(hist, clt.cluster_centers_)
    
    plt.figure()
    plt.axis("off")
    plt.imshow(bar)
    plt.show()

image_path = "/content/drive/MyDrive/sample (1)/3. background remove/1.jpg"

#preview image
image = mpimg.imread(image_path)
plt.imshow(image)

image_color_cluster(image_path)

images = [
    '/content/drive/MyDrive/sample (1)/3. background remove/1.jpg',
    '/content/drive/MyDrive/sample (1)/3. background remove/2.jpg',
    '/content/drive/MyDrive/sample (1)/3. background remove/3.jpg',
    '/content/drive/MyDrive/sample (1)/3. background remove/4.jpg',
    '/content/drive/MyDrive/sample (1)/3. background remove/5.jpg'
]


for image_path in images:
    image = mpimg.imread(image_path)
    plt.imshow(image)

    image_color_cluster(image_path)

k = 5 # 예제는 5개로.
    clt = KMeans(n_clusters = k)  # 평균 알고리즘 KMeans
    clt.fit(image)
    

    hist = centroid_histogram(clt)
    bar = plot_colors(hist, clt.cluster_centers_)
    return bar


    def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    #히스토그램 형식으로 색을 반환
    #based on the number of pixels assigned to each cluster
    #각 클러스터의 픽셀의 숫자를 기반으로 함
        numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
        (hist, _) = np.histogram(clt.labels_, bins=numLabels)

        # normalize the histogram, such that it sums to one
        hist = hist.astype("float")
        hist /= hist.sum()  # hist = hist/hist.sum()

        # return the histogram
        return hist

#추출한 color와 histogram 데이터로 화면에 그래프를 그리는 코드
    hist = centroid_histogram(clt)
    print(hist)
    #[ 0.68881873  0.09307065  0.14797794  0.04675512  0.02337756]

    def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
    # of each of the colors
        bar = np.zeros((50, 300, 3), dtype="uint8")
        startX = 0

    # loop over the percentage of each cluster and the color of
    # each cluster
        for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
            endX = startX + (percent * 300)
            cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                        color.astype("uint8").tolist(), -1)
            startX = endX

    # return the bar chart
        return bar

    bar = plot_colors(hist, clt.cluster_centers_)

    # show our color bart
    plt.figure()
    plt.axis("off")
    plt.imshow(bar)
    plt.show()

#2. 대표색 16진수로 남기기

def read_real_color(filename):
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image_list = [str(list(image[i][k])) for i in range(len(image)) for k in range(len(image[0]))]
    image_unique = {}
    for d in image_list:
        if d not in image_unique:
            image_unique[d] = 1
        else:
            image_unique[d] += 1

    import operator
    icon_color_list = max(image_unique.items(), key=operator.itemgetter(1))[0]

    color_R = int(icon_color_list.split('[')[1].split(']')[0].split(', ')[0])
    color_G = int(icon_color_list.split('[')[1].split(']')[0].split(', ')[1])
    color_B = int(icon_color_list.split('[')[1].split(']')[0].split(', ')[2])

    color_R = dec_to_hex(color_R)
    color_G = dec_to_hex(color_G)
    color_B = dec_to_hex(color_B)

    return str(color_R + color_G + color_B)

def dec_to_hex(color):
    if color < 16:
        return '0' + str(hex(int(color)).split('x')[1])
    else:
        return str(hex(int(color)).split('x')[1])

color_list = []
for n in df_cafe.index:
    png = './cafe_color_result/' + df_cafe['파일명'][n]
    color_list.append(read_real_color(png))
df_cafe['대표색'] = color_list