#JOBLIB.py
from joblib import Parallel, delayed
import math

#병렬로 실행할 함수
def process(i):
    return math.sqrt(i)

#Parallel객체를 이용하여, 함수실행을 병렬로 처리
result = Parallel(n_jobs=2)(delayed(process)(i) for i in range(10))
print(result)