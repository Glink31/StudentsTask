from menu_item import MenuItem
class SimpleMenuItem(MenuItem):
    def __init__(self,title,command):
        super().__init__(title)     
        self.__command = command
    def run(self):
        self.__command()