#DASK,py
import dask.array as da

#큰 Dask 배열 생성
x = da.random.random((10000,10000),chunks=(1000,1000))

#배열에 대한 연산수행
y = x + x.T

#평균계산
z = y.mean(axis=0)

#계산실행
result = z.compute()
print(result)