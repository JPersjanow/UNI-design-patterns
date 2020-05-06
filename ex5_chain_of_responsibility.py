import abc
import multiprocessing
import time

class TakesTooLongError(Exception):
    pass

class CalculationMethods:
    def cube_method(x: list, raise_exception: bool) -> float:
        n = len(x)
        max_now = 0
        for i in range(0, n-1, 1):
            for j in range(i, n-1, 1):
                summ = 0
                for k in range (i, j, 1):
                    summ += x[k]
                    max_now = max(max_now, summ)
        if raise_exception:
            raise TakesTooLongError
        else:
            print(max_now)

    def square_method(x: list, raise_exception: bool) -> float:
        n = len(x)
        max_now = 0
        for i in range(0, n-1, 1):
            summ = 0
            for j in range(i, n-1, 1):
                summ += x[j]
                max_now = max(max_now, summ)
        if raise_exception:
            raise TakesTooLongError
        else:
            print(max_now)

    def linear_method(x: list, raise_exception: bool) -> float:
        n = len(x)
        max_sofar = 0
        max_here = 0
        for i in range(0, n-1, 1):
            max_here = max(max_here + x[i], 0)
            max_sofar = max(max_sofar, max_here)

        if raise_exception:
            raise TakesTooLongError
        else:
            print(max_sofar)



class Handler(metaclass=abc.ABCMeta):
    def __init__(self, successor=None, lista=[], max_time_wait=0.5):
        self._successor = successor
        self.lista = lista
        self.max_time_wait = max_time_wait

    @abc.abstractmethod
    def handle_request(self):
        pass

class LinearHandler(Handler):
    def handle_request(self):
        try:
            CalculationMethods.linear_method(self.lista, raise_exception=False)
        except TakesTooLongError:
            print("Took too long! Linear Handler failed!")
            if self._successor is not None:
                self._successor.handle_request()
            else:
                print("No succesor set, aborting operation!")
    def handle_request_withTimer(self):
        proc = multiprocessing.Process(target=CalculationMethods.linear_method(self.lista), daemon=True)
        proc.start()
        proc.join(self.max_time_wait)

        if proc.is_alive():
            print("Takes too long changing handler")
            proc.terminate()
            if self._successor is not None:
                self._successor.handle_request()
            else:
                print("No succesor set, aborting operation!")

class SquareHandler(Handler):
    def handle_request(self):
        try:
            CalculationMethods.square_method(self.lista, raise_exception=True)
        except TakesTooLongError:
            print("Took too long! Square Handler failed!")
            if self._successor is not None:
                self._successor.handle_request()
            else:
                print("No succesor set, aborting operation!")
    def handle_request_withTimer(self):
        proc = multiprocessing.Process(target=CalculationMethods.square_method(self.lista), daemon=True)
        proc.start()
        proc.join(self.max_time_wait)

        if proc.is_alive():
            print("Takes too long changing handler")
            proc.terminate()
            if self._successor is not None:
                self._successor.handle_request()
            else:
                print("No succesor set, aborting operation!")

class CubeHandler(Handler):
    def handle_request(self):
        try:
            CalculationMethods.cube_method(self.lista, raise_exception=True)
        except TakesTooLongError:
            print("Took too long! Cube Handler failed!")
            if self._successor is not None:
                self._successor.handle_request()
            else:
                print("No succesor set, aborting operation!")
    def handle_request_withTimer(self):
        proc = multiprocessing.Process(target=CalculationMethods.cube_method(self.lista), daemon=True)
        proc.start()
        proc.join(self.max_time_wait)

        if proc.is_alive():
            print("Takes too long changing handler")
            proc.terminate()
            if self._successor is not None:
                self._successor.handle_request()
            else:
                print("No succesor set, aborting operation!")

if __name__ == '__main__':
    lista = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84, 31, -41, 59, 26, -53, 58, 97, -93, -23, 84, 31, -41, 59, 26, -53, 58, 97, -93, -23, 84,
             31, -41, 59, 26, -53, 58, 97, -93, -23, 84,31, -41, 59, 26, -53, 58, 97, -93, -23, 84, 31, -41, 59, 26, -53, 58, 97, -93, -23, 84,
             31, -41, 59, 26, -53, 58, 97, -93, -23, 84, 31, -41, 59, 26, -53, 58, 97, -93, -23, 84, 31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    handler1 = LinearHandler(lista=lista)
    handler2 = SquareHandler(lista=lista, successor=handler1)
    handler3 = CubeHandler(lista=lista, successor=handler2)
    handler3.handle_request()