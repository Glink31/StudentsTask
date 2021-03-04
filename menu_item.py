from abc import ABCMeta, abstractmethod
class MenuItem(metaclass=ABCMeta):
    def __init__(self,title):
        self.__title = title

    @property
    def title(self):
        return self.__title

    @abstractmethod
    def run(self):
        pass
