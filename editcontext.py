from singleton import Singleton
class EditContext(metaclass=Singleton):
    def __init__(self):
        self.student = None 