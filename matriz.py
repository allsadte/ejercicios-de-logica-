class Matrix:

    def __init__(self, lista):
        self.matriz = lista

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







