#SHAPELY.py
from shapely.geometry import Polygon

#사각형 폴리곤 생성
polygon = Polygon([(0,0),(1,0),(1,1),(0,1)])
print("Polygon area: ",polygon.area) #면적출력

#폴리곤의 경계선 출력
print("Polygon boundary : ",polygon.boundary)
