import boto3
import glob
import os

 #s3 client 생성(따로 만질 필요 없습니다.)
def s3_connection():
    try:
       
        s3 = boto3.client(
            service_name ="s3",
            region_name = "ap-northeast-2",
            aws_access_key_id="AKIAWBWA5G56T4MJYXVL",
            aws_secret_access_key="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"

        )

    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!")
        return s3
#s3 변수로 aws 스토리지에 접근
s3 = s3_connection()

# 이미지 파일 다운로드 하는 법 => s3.download_file("ktai","{이미지파일이름.확장자}","{저장할 경로/파일이름.확장자}")

#밑에는 사용예시입니다. 주석제거하고 사용하시면 됩니다.(ktai는 설정한 storage 이름이라 꼭 넣어야 합니다.)
# s3.download_file("ktai","abandoned1.jpg","./6/result/test1.jpg")
