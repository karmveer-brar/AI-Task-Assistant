import random
import datetime

class SimpleAI:
    def greet(self):
        return "Hello! I am your simple AI assistant."

    def do_math(self, a, b):
        return f"The sum of {a} and {b} is {a+b}"

    def tell_time(self):
        return f"Current time is {datetime.datetime.now().strftime('%H:%M:%S')}"

    def decide_action(self):
        actions = ["eat", "work", "rest", "study"]
        return f"I think you should {random.choice(actions)}."

# Demo run
ai = SimpleAI()
print(ai.greet())
print(ai.do_math(5, 7))
print(ai.tell_time())
print(ai.decide_action())
