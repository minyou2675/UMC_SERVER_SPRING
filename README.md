# KT-SMU-AI-project-
2022 KT와 함께하는 상명 AI 경진대회

Ani - Time팀 깃허브 입니다.

# Ani -Time 
## AI 를 활용한 유기견 모니터링 시스템

<p align="center">
  <br>
  <img width="50%" src="https://user-images.githubusercontent.com/79439483/187695733-9de05769-f9e3-4e41-8063-7d1c0e246000.jpg">
  <br>
</p>

목차

## 팀원 소개

<p align="center">
  <br>
  <img width="50%" src="https://user-images.githubusercontent.com/79439483/187695071-a0f6b7a3-7016-4b4b-801a-b095b3eeaea9.jpg"/>
  <br>
</p>


## 프로젝트 개요/동기
</p>

<p align="center">
  
 - 유기견 개체 수 증가
  
 - 유기견으로 인한 사회적 문제 증가
  
 - 개체수 관리의 어려움
</p>

<br>

## 기술 스택


|  객체 탐지  | 배경 제거 |  특징 추출   |  데이터베이스   |
| :--------: | :--------: | :------: | :-----: |
| <img width="80%" src="https://user-images.githubusercontent.com/79439483/187697100-4d0f969d-e1b5-431c-aa12-95b7ac6bb59b.jpg"/>  |   <img width="80%" src="https://user-images.githubusercontent.com/79439483/187698245-09f1f455-199d-491f-80e8-e1bf132beae1.jpg"/>    | - K-means 알고리즘 <br> -EfficentNet <br>  | <img width="20%" src="https://user-images.githubusercontent.com/79439483/187699076-8dad0f10-7dda-454d-9642-524aa7d482b3.jpg"/> <img width="20%" src="https://user-images.githubusercontent.com/79439483/187699784-15097247-aa86-46e8-9aa5-93c72d3dcc5a.jpg"/>|

<br>

## 구현 기능

### 기능 1 

 - 데이터 셋 구축
 - 출처: 동물 보호 관리 시스템
 - 개체수 관리의 어려움


### 기능 2

 - 객체 탐지
 - 제보 받은 영상은 다양한 객체가 같이 찍히기 때문에 YOLOv5 모델을 이용함

### 기능 3

 - 배경 제거
 - 정확한 분석을 위해 배경을 제거함
 
### 기능 4

 - 특징 추출
 - K-means 알고리즘을 이용하여 컬러클러스터링을 진행하였고, EfficientNet 을 이용하여 70%정확도의 견종 예측을 완성시킴

### 기능 5

 - 데이터베이스
 - MySQL을 이용하여 정형데이터를 관리하였고, AWS 기반 S3 를 이용하여 비정형 데이터를 관리하였음

### 기능 6

 - 유사도 분석
 - cv2.HISTCMP_CORREL, cv2.HISTCMP_INTERSECT, cv2.HISTCMP_CHISQR, cv2.HISTCMP_BA\HATTACHARYYA, EMD 등의 함수를 이용하여 실종견 이미지 간의 유사도를 분석함

### 기능 7

 - 지도시각화
 - 데이터 베이스 내의 구별 유기겨 현황을 지도로 시각화하여, 한눈에 어느 구에서 많은 유기견이 발생하는지 파악할 수 있으며, 손쉽게 관리 가능하도록 함


## 배운 점 & 아쉬운 점

 - 지도시각화
 - 데이터 베이스 내의 구별 유기겨 현황을 지도로 시각화하여, 한눈에 어느 구에서 많은 유기견이 발생하는지 파악할 수 있으며, 손쉽게 관리 가능하도록 함


## 기대효과

 - 유기견과 시민 모두의 안전 확보
 - 동물유기에 대한 경각심 재고
 - 유기견에 의한 생태계 혼란 방지
 - 유기견에 의한 사회적 비용 감소

## 발전방향

 - 유기동물 종류 추가
 - 유기동물 발생 원인 예측 시스템 구축
 - 실시간 CCTV 영상을 이용한 모니터링
 - 봉사단체와 연계하여 자원 봉사자 파견


## 라이센스


