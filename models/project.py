from utils.image_loader import ImageHandler

class Project():
    def __init__(self, id: int, project_path: str) -> None:
        self.__id = id
        self.__project_path = project_path
        self.__dataset_path = f"{self.__project_path}/dataset"
        self.__exported_data_path = f"{self.__project_path}/exported-data"
        self.__polygon_data_path = f"{self.__project_path}/polygon-data"
        self.image_loader = ImageHandler
    
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def project_path(self) -> str:
        return self.__project_path
    
    @property
    def dataset_path(self) -> str:
        return self.__dataset_path
    
    @property
    def exported_data_path(self) -> str:
        return self.__exported_data_path
    
    @property
    def polygon_data_path(self) -> str:
        return self.__polygon_data_path
