from __future__ import annotations
from uuid import uuid4


class Task:
    def __init__(self, name, category_id = None, project_id = None):
        self.id = uuid4()
        self.name = name
        self.category_id = category_id
        self.project_id = project_id

class Category:
    def __init__(self, name):
        self.id = uuid4()
        self.name = name

class Project:
    def __init__(self, name, category_id = None):
        self.id = uuid4()
        self.name = name
        self.category_id = category_id
   
class Note:
    def __init__(self, name, contents, category_id = None, project_id = None):
        self.id = uuid4()
        self.name = name
        self.contents = contents
        self.category_id = category_id
        self.project_id = project_id

