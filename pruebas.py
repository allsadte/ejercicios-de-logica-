import matriz


a = [1, 2]
b = [[1, 2], [2, 4]]
c = [[1, 2], [2, 4], [2, 4]]
d = [[[3, 4], [6, 5]]]
e = [[[1, 2, 3]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3], [2, 3]]]
f = [[[1, 2, 3], [2, 3, 4]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3]]]

o = matriz.Matrix(a)
print('profundidad ', o.dimension())
print('suma ', o.compute())
print("balanceado", o.balanced())
o = matriz.Matrix(b)
print('profundidad ', o.dimension())
print('suma ', o.compute())
print("balanceado", o.balanced())
o = matriz.Matrix(c)
print('profundidad ', o.dimension())
print('suma ', o.compute())
print("balanceado", o.balanced())
o = matriz.Matrix(d)
print('profundidad ', o.dimension())
print('suma ', o.compute())
print("balanceado", o.balanced())
o = matriz.Matrix(e)
print('profundidad ', o.dimension())
print('suma ', o.compute())
print("balanceado", o.balanced())
o = matriz.Matrix(f)
print('profundidad ', o.dimension())
print('suma ', o.compute())
print("balanceado", o.balanced())
