#RAY,py
import ray

#Ray 초기화
ray.init()

#Ray를 사용하여 병렬실행할 함수를 정의
@ray.remote
def f(x):
    return x * x

#병렬로 함수를 실행하고, 결과를 가져오기
futures = [f.remote(i) for i in range(10)]
print(ray.get(futures))