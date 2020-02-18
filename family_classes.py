class Kid:
     def __init__(self, name=None, age=-1):
         self.name = name
         self.age = age

class Family:
     def __init__(self, parents=[]):
         self.parents = parents
         self.kids = []

     def add_kid(self, kid=None):
         self.kids.append(kid)