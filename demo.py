
# list_a = [a ** 2 for a in range(6)]
# print(list_a)
#
# genera_a = (a ** 2 for a in range(6))

def genera_func():
    yield 1

g=genera_func()
print(next(g))
# 执行器
#方法

