class Category:
    def __init__(self, name : str, color : str):
        self.__name = name
        self.__color = color
    
    def __init__(self):
        self.__name = ''
        self.__color = ''
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
    
    @property
    def color(self) -> str:
        return self.__color
    
    @color.setter
    def color(self, color: str) -> None:
        self.__color = color
