a = [1, 2]
b = [[1, 2], [2, 4]]
c = [[1, 2], [2, 4], [2, 4]]
d = [[[3, 4], [6, 5]]]
e = [[[1, 2, 3]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3], [2, 3]]]
f = [[[1, 2, 3], [2, 3, 4]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3]]]


class Matrix:

    def __init__(self, arreglo):
        self.matriz = arreglo

    def get_matriz(self):
        return self.matriz


    def list_of_elements(self, matriz, elements):
        if type(matriz) == list:
            for i in range(len(matriz)):
                self.list_of_elements(matriz[i], elements)
        if type(matriz) == int:
            elements.append(matriz)

    def compute(self):
        elements = []
        self.list_of_elements(self.matriz, elements)
        total = 0
        for i in range(len(elements)):
            total = total + elements[i]
        return total

    def __list_of_deeps(self, matriz, floor, deeps):
        if type(matriz) != int:
            for i in range(len(matriz)):
                if type(matriz[i]) == int:
                    floor = floor + 1
                    deeps.append(floor)
                    break
                self.__list_of_deeps(matriz[i], floor + 1, deeps)

    def dimension(self):
        deeps = []
        self.__list_of_deeps(self.matriz, 0, deeps)
        return max(deeps)

    def __list_of_balanced(self, matriz, balance):
        if type(matriz) != int:
            for i in range(len(matriz)):
                if type(matriz[i]) == int:
                    balance.append(len(matriz))
                    break
                self.__list_of_balanced(matriz[i], balance)

    def balanced(self):
        balance = []
        estatus = False
        self.__list_of_balanced(self.matriz, balance)
        for i in balance:
            if i == balance[0]:
                estatus = True
            else:
                estatus = False
                break
        return estatus



n= []
o = Matrix(f)
n=o.balanced()
print(n)


'''o = Matrix(a)
print('profundidad ' + str(o.dimension()))
print('suma ' + str(o.compute()))
o = Matrix(b)
print('profundidad ' + str(o.dimension()))
print('suma ' + str(o.compute()))
o = Matrix(c)
print('profundidad ' + str(o.dimension()))
print('suma ' + str(o.compute()))
o = Matrix(d)
print('profundidad ' + str(o.dimension()))
print('suma ' + str(o.compute()))
o = Matrix(e)
print('profundidad ' + str(o.dimension()))
print('suma ' + str(o.compute()))
o = Matrix(f)
print('profundidad ' + str(o.dimension()))
print('suma ' + str(o.compute()))
'''
