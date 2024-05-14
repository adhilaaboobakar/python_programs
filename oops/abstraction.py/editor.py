from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class VScode(Editor):

    def edit(self):
        print("VS code edits")

    def debug(self):
        print("VS code debugs")

    def execute(self):
        print("VS code executes")

vsc=VScode()
vsc.edit()