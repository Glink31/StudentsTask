from menu_item import MenuItem
from simple_menu_item import SimpleMenuItem
class Menu(MenuItem):
    def __init__(self, title="", is_submenu=False):
        super().__init__(title)  
        self.__items = []
        self.is_submenu = is_submenu
        self.__onStartCommand = None
        self.__beforeSelectedCommand = None
        self.__onFinishCommand = None
    def additem(self,title,command):
        self.__items.append(SimpleMenuItem(title,command))
    def addSubmenu(self,title):
        menu = Menu(title,is_submenu=True)
        self.__items.append(menu)
        return menu

    @property
    def onStartCommand(self):
        return self.__onStartCommand
    @property
    def beforeSelectedCommand(self):
        return self.__beforeSelectedCommand
    @property
    def onFinishCommand(self):
        return self.__onFinishCommand
    @onStartCommand.setter
    def onStartCommand(self,command):
        self.__onStartCommand = command
    @beforeSelectedCommand.setter
    def beforeSelectedCommand(self,command):
        self.__beforeSelectedCommand = command
    @onFinishCommand.setter
    def onFinishCommand(self,command):
        self.__onFinishCommand = command
    def run(self):
        keep = True
        if self.__onStartCommand is not None:
            if not self.__onStartCommand():
                return
        while keep:
            if self.__beforeSelectedCommand is not None:
                self.__beforeSelectedCommand()
            self.printMenu()
            keep = self.handleUserInput()
        if self.__onFinishCommand is not None:
            self.__onFinishCommand()
    def printMenu(self):
        for i,x in enumerate(self.__items):
            print(f"{i+1}.{x.title}")
        if not self.is_submenu:
            print(f"{len(self.__items)+1}.Выход")
        else:
            print(f"{len(self.__items)+1}.Назад")
    def handleUserInput(self):
        inp = int(input("Выберите пункт меню: "))
        if inp <= 0 or inp > len(self.__items)+1:
            print("Ввод неверен")
            return True
        elif inp == len(self.__items)+1:
            return False
        else:
            self.__items[inp-1].run()
            return True
                