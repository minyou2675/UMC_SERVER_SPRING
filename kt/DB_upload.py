import pymysql.cursors
import csv

#mysql 연결

conn = pymysql.connect(
    host='database-2.cdv8ov56qedi.ap-northeast-2.rds.amazonaws.com',
    user='admin',
    password='sjw04050',
    db='KTDB',
    charset='utf8')

curs=conn.cursor()

sql = """
    INSERT INTO puppy (imagenum,filename,date,location,breed,shelter,width,height) values(%s, %s, %s,%s,%s,%s,%s,%s)
"""

f=open('abandoned_dog_sample.csv','r',encoding='utf-8')
rd=csv.reader(f)

for line in rd:
    curs.execute(sql,(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]))

conn.commit()
conn.close()
f.close()


