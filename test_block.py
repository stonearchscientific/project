import pytest
import block

def test_add_task():
    task_block = block.Task(["Name", "Lead", "Start", "End"])
    task_block.add_task(Name="Task 1", Lead="Bob", Start="1/1/2020", End="1/2/2020")

    assert task_block.width() == 4
    assert task_block.height() == 1
    assert task_block.tasks.iloc[0]["Name"] == "Task 1"
    assert task_block.tasks.iloc[0]["Start"] == "1/1/2020"

    task_block.add_task(Name="Task 2", Lead="Karen", End="1/2/2020", Start="1/1/2020")

    assert task_block.width() == 4
    assert task_block.height() == 2
    assert task_block.tasks.shape == (2, 4)
    assert task_block.tasks.iloc[1]["Name"] == "Task 2"
    assert task_block.tasks.iloc[1]["Start"] == "1/1/2020"

