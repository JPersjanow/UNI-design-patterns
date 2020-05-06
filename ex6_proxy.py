from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from random import randrange

class Keyboard(ABC):
    #available keys to update and cycle through
    available_keys = ["a", "b", "c", "q"]
    key_pressed = None
    _observers: List[Key] = []
    instance = None


    @staticmethod
    def getInstance():
        if Keyboard.instance == None:
            Keyboard()
        return Keyboard()

    def __init__(self):
        if Keyboard.instance != None:
            raise Exception("This is a singleton class")
        else:
            Keyboard.instance = self

    def attach(self, observer: Key) -> None:
        if observer.subject is not None:
            print("Attached")
            self._observers.append(observer)

    def detach(self, observer: Key) -> None:
        print("Detached")
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Notifying observers")
        for observer in self._observers:
            observer.update(self)

    def change_key(self) -> None:
        print("Changing key")
        self.key_pressed = self.available_keys[randrange(0, len(self.available_keys))]

        print(f"Pressed key is now {self.key_pressed}")
        self.notify()

class Key(ABC):
    def __init__(self, key: str):
        self.key = key

    def update(self, subject: Keyboard) -> None:
        if subject.key_pressed == self.key:
            print(f"Key {self.key} pressed")
            subject.detach(self)

class Proxy:
    def __init__(self, subject):
        if subject in ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']:
            self.subject = Key(subject)
        else:
            self.subject = None

class KeyProxy(Proxy):

    def update(self, subject: Keyboard) -> None:
        if subject.key_pressed == self.subject.key:
            print(f"Key {self.subject.key} pressed")
            subject.detach(self)


if __name__ == "__main__":
    keyboard = Keyboard()
    k1 = KeyProxy("a")
    k2 = KeyProxy("b")
    k3 = KeyProxy("q")
    k4 = KeyProxy("d")
    keyboard.attach(k1)
    keyboard.attach(k2)
    keyboard.attach(k3)
    keyboard.attach(k4)

    while keyboard._observers:
        keyboard.change_key()