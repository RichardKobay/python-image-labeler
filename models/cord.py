class Cord:
    def __init__(self, x : float, y : float, is_root: bool) -> None:
        self.__x = x
        self.__y = y
        self.__is_root = is_root
    
    @property
    def x (self) -> float:
        return self.__x
    
    @property
    def y (self) -> float:
        return self.__y
    
    @property
    def is_root (self) -> bool:
        return self.__is_root
