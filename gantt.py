import xlwings as xw
import pandas as pd
import block
from datetime import date

class Gantt:
    def __init__(self, title=None, task_labels=None, project_start=None, project_end=None):
        if task_labels is None:
            task_labels = ["Name", "Start", "End", "Duration"]
        self.task_block = block.Task(task_labels)

        self.project_block = block.Project(title)
        if project_start is None:
            self.project_block.start = date.today()
        if project_end is None:
            self.project_block.end = date.today() + pd.DateOffset(days=365)
        self.project_block.right = self.task_block.right

    def draw(self):
        print("Drawing Gantt chart")
        # Draw the chart
