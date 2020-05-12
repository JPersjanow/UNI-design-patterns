import abc
import random

class AbstractAlgorythm(abc.ABC):
    def __init__(self, n:int, m:int):
        self.n = n
        self.m = m
        self.result = []

    @abc.abstractmethod
    def solve(self):
        pass

class AbstractFactory(abc.ABC):
    def __init__(self, n:int, m:int, sort:bool):
        self.n = n
        self.m = m
        self.sort = sort

    @abc.abstractmethod
    def solve_algorythm(self):
        pass

class Factory(AbstractFactory):
    def solve_algorythm(self):
        if self.sort == True:
            return AlgorythmB(self.n, self.m)
        else:
            if self.n - self.m <= 2:
                return AlgorythmA(self.n, self.m)
            else:
                return AlgorythmC(self.n, self.m)

class AlgorythmA(AbstractAlgorythm):
    def __init__(self, n:int, m:int):
        super().__init__(n, m)
        self.result = []

    def solve(self):
        for i in range(0, self.m):
            repeat = True
            while repeat == True:
                rand_number = random.randint(1, self.n)

                if rand_number in self.result:
                    repeat = True
                else:
                    self.result.append(rand_number)
                    repeat = False

        # self.result.sort()

class AlgorythmB(AbstractAlgorythm):
    def __init__(self, n:int, m:int):
        super().__init__(n, m)
        self.result = []

    def solve(self):
        choose = self.m
        left = self.n
        for i in range(1, self.n + 1, 1):
            probability = choose / left
            rand_number = random.uniform(0,1)

            if rand_number < probability:
                choose -= 1
                self.result.append(i)

            left -= 1

class AlgorythmC(AbstractAlgorythm):
    def __init__(self, n:int, m:int):
        super().__init__(n, m)
        self.result = []

    def solve(self):
        table = []
        for i in range(1, self.n+1, 1):
            table.append(i)

        for j in range(1, self.m, 1):
            rand_number = random.randint(1, self.n-1)
            if table[j] != j:
                table[j] = table[rand_number]

        for k in range(0, self.m, 1):
            self.result.append(table[k])

if __name__ == '__main__':
    factory = Factory(10, 6, False)
    alg = factory.solve_algorythm()
    alg.solve()
    print(alg.result)