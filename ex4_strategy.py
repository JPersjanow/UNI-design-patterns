import abc
class Strategy(abc.ABC):
    def execute(self):
        return "Strategy"

class StrategyBike(Strategy):
    def __init__(self):
        self.cost = 0
        self.time = 60
        self.risk = 'high'

    def execute(self):
        return "Using bike!"

class StrategyPublicCommunication(Strategy):
    def __init__(self):
        self.cost = 3
        self.time = 30
        self.risk = 'medium'

    def execute(self):
        return "Using Public Transport!"

class StrategyTaxi(Strategy):
    def __init__(self):
        self.cost = 20
        self.time = 15
        self.risk = 'low'

    def execute(self):
        return "Using Taxi!"

class Context:
    __strategy: Strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def execute_strategy(self):
        return self.strategy.execute()

class Application:

    def __init__(self, available_cost: int, available_time: int, object_value: str):
        self.available_cost = available_cost
        self.available_time = available_time
        self.object_value = object_value
        self.context = Context()

    def run(self):
        if 0 <= self.available_cost <= 3 and self.available_time >= 60 and self.object_value == 'low':
            self.context.set_strategy(StrategyBike())
            return self.context.execute_strategy()
        elif 3 <= self.available_cost <= 20 and 60 > self.available_time >= 30 and self.object_value == 'medium':
            self.context.set_strategy(StrategyPublicCommunication())
            return self.context.execute_strategy()
        elif self.available_cost >= 20 and 15 <= self.available_time < 30 and self.object_value == 'high':
            self.context.set_strategy(StrategyTaxi())
            return self.context.execute_strategy()
        else:
            return "No available strategy"

if __name__ == "__main__":
    available_cost = int(input("Insert how much you want to spend (whole number):"))
    available_time = int(input("Insert how much time do you have (in minutes without seconds!):"))
    object_value = input("Insert how valuable is object (low, medium, high)")

    if object_value not in ['low', 'medium', 'high']:
        print("wrong object value! Insert again (low, medium, high)")
        object_value = input("Insert how valuable is object (low, medium, high)")

    a = Application(available_cost, available_time, object_value)
    print(a.run())