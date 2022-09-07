from fileinput import filename
import boto3
import glob
import os
class s3_create:
 #s3 client 생성(따로 만질 필요 없습니다.)
    def __init__(self):
        try:
            self.s3 = boto3.client(
            service_name ="s3",
            region_name = "ap-northeast-2",
            aws_access_key_id="AKIAWBWA5G56T4MJYXVL",
            aws_secret_access_key="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"
            )

        except Exception as e:
            print(e)
        else:
            print("s3 bucket connected!")
            
          
    #s3 변수로 aws 스토리지에 접근
    # self.s3 = self.s3_connection()

    # 이미지 파일 다운로드 하는 법 => s3.download_file("ktai","{찾고싶은 이미지파일이름.확장자}","{찾은 이미지 파일을 저장할 경로/설정할 파일이름.확장자}")

    #밑에는 이미지 다운로드시 사용예시입니다. 주석제거하고 사용하시면 됩니다.(ktai는 설정한 storage 이름이라 꼭 넣어야 합니다.)
    #s3.download_file("ktai","abandoned1.jpg","./test1.jpg")
    def download(self,file_path,save_path):
        self.s3.download_file("ktai",file_path,save_path)
        self.s3.close()
    #s3에 이미지 업로드 하는법 => s3.upload_file("{로컬에서 올릴 파일경로+이름.확장자}","ktai","{스토리지에 저장될 파일 이름+확장자}")

    def upload(self,file_path,save_path):
        self.s3.upload_file(file_path,"ktai",save_path)
        self.s3.close()
    # i=41
    # for i in range(41,81):
    #     s3.upload_file(f"./유기견/abandoned{i}.jpg","ktai",f"abandoned{i}.jpg")
    #     i += 1



# 전체 데이터 불러오는 법 =>
    def getObjectList(self):
        filename = []
        object_list = self.s3.list_objects(Bucket="ktai",Prefix="prefix")
        while 'contents' in object_list.keys():
            object_contents = object_list['contents']
            for i in range(len(object_contents)):
                filename = object_contents[i]['key']
        return filename

# for item in contents_list:
#     print(item)
