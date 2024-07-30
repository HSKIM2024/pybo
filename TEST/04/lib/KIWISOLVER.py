#KIWISOLVER.py
from kiwisolver import Solver, Variable

#변수생성
x = Variable("x")
y = Variable("y")

#솔버 인스턴스생성
solver = Solver()

#제약조건 추가: x + y == 10
solver.addConstraint(x + y == 10)

#추가제약조건: x * 2 == y
solver.addConstraint(x * 2 == y)

#문제해결
solver.updateVariables()

#결과출력
print(f"x: {x.value()}, Y:{y.value()}")
