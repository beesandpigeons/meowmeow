import datetime
class Task:
    def __init__(self, title, priority, due_date):
    self.title = title
    self.priority = priority
    self.due_date = due_date
    self.completed = False
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def complete_task(self, task):
        task.completed = True

class Reminder:
    def __init__(self, task, reminder_time):
        self.task = task
        self.reminder_time = reminder_time
    def remind(self):
        print("Reminder")
