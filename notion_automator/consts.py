import os


NOTION_TOKEN = os.environ["NOTION_TOKEN"]
TASKS_DATABASE_ID = os.environ["TASKS_DATABASE_ID"]

class TasksProp:
    TASK = "Task"
    STATE = "State"
    DONE = "Done"
    DUE = "Due"
    NEXT_DUE = "Next Due"

    ALL = [TASK, STATE, DONE, DUE, NEXT_DUE]
