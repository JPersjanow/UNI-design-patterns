class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Keyboard(metaclass=Singleton):
    def __init__(self, key_pressed: str):
        self.key_pressed = key_pressed

class Key:
    def __init__(self, key):
        self.key = key




