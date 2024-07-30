#GEOPANDAS.py
import geopandas as gpd
from geodatasets import get_path
import matplotlib.pyplot as plt

#공간데이터 파일읽기
gdf = gpd.read_file(get_path("geoda airbnb"))

#GeoDataFrame 출력
print(gdf.columns)
print(gdf.head())

#기본적인 데이터시각화
gdf.plot("price_pp",legend=True)
plt.show()