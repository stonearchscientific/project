import xlwings as xw
import pandas as pd

class Block:
    def __init__(self):
        self.upper = 0
        self.lower = 0
        self.left = 0
        self.right = 0

    def height(self):
        return self.lower - self.upper

    def width(self):
        return self.right - self.left


class Project(Block):
    def __init__(self, name):
        super().__init__()
        self.name = name

class Task(Block):
    def __init__(self, labels):
        super().__init__()
        self.tasks = pd.DataFrame(columns=labels)
        self.right = self.tasks.shape[1]

    def add_task(self, **info):
        task = pd.DataFrame([info], index=[0])
        self.tasks = pd.concat([self.tasks, task], ignore_index=True)
        self.lower = self.tasks.shape[0]

class Event(Block):
    def __init__(self, name):
        super().__init__(name)

class Calendar(Block):
    def __init__(self, name):
        super().__init__(name)

class Gantt:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print("Drawing Gantt chart")
        # Draw the chart
