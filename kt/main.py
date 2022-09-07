import dog_breed_classification
import s3
import os
import torch
import pandas as pd
import glob
import cv2
import pymysql
import csv


#경로 설정
file_path="./data"
file_list = os.listdir(file_path)


#1. Detection 
detection = torch.hub.load('./detection','custom', './detection/normal.pt', source='local')
# images = glob.glob('./data/*.jpg')
results = detection(file_list)

results.save()
crops = results.crop(save=True)
os.system('python ./detection/detect.py --weights ./detection/best.pt --img 640 --conf 0.5 --source ./data ')

#2. 배경제거
os.system('python background_remove.py')

#3. 크기 추출
os.system('python size.py')

#4. 견종분류
model = dog_breed_classification.models()
breed_data = model.export(file_path)

#5. 모색 클러스터링

#기존 엑셀 파일 합침

# df = pd.read_excel('abandoned_dog_sample.xlsx')
# df['filename'] = df['filename'] + '.jpg'
df_size = pd.read_excel('./output/3.size/size.xlsx')
# df = df.merge(df_size, how="outer", on='filename')
accuracy = pd.read_excel('accuracy.xlsx')
output = df_size.merge(accuracy,how="outer",on='filename')
output = output.merge(breed_data,how="outer",on='filename')

# data_results.to_excel("./database2.xlsx")
output['accuracy'].replace('tensor','',inplace=True)
output = output.drop('Unnamed: 0', axis=1)
output.to_excel("./output/output.xlsx") #breed + 정확도 데이터#breed + 정확도 데이터

#6.(정형 데이터) 데베에 업로드

conn = pymysql.connect(
    host='database-2.cdv8ov56qedi.ap-northeast-2.rds.amazonaws.com',
    user='admin',
    password='sjw04050',
    db='KTDB',
    charset='utf8')

curs=conn.cursor()

sql = """
    INSERT INTO puppy (imagenum,filename,date,location,breed,shelter,width,height,accuracy) values(%s, %s, %s,%s,%s,%s,%s,%s,%s)
"""

f=open('output.xlsx','r',encoding='utf-8')
rd=csv.reader(f)

for line in rd:
     curs.execute(sql,(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10]))

conn.commit()
conn.close()
f.close()




# 7.(비정형 데이터) 데베에 업로드
s3 = s3.s3_create()

for i in file_list:   
    s3.upload(file_path/+file_list,file_list)
