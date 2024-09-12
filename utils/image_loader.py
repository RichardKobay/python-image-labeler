import os
import glob
from PIL import Image

class ImageHandler:
    def __init__(self, project_path: str) -> None:
        self.__images = []
        self.__project_path = project_path
        self.__dataset_path = os.path.join(self.__project_path, 'dataset')
        self.__image_extensions = ('*.png', '*.jpg', '*.jpeg')
        os.makedirs(self.__dataset_path, exist_ok=True)

    @property
    def images(self) -> list:
        return self.__images

    def load_dataset(self, path: str) -> None:
        self.__images.clear()
        self.__clear_dataset()

        for extension in self.__image_extensions:
            for image_path in glob.glob(os.path.join(path, extension)):
                with Image.open(image_path) as img:
                    image_name = os.path.splitext(os.path.basename(image_path))[0]
                    new_image_path = os.path.join(self.__dataset_path, f"{image_name}.png")
                    img.convert("RGB").save(new_image_path, "PNG")
                    self.__images.append(f"{image_name}.png")

    def load_images(self, paths: list) -> None:
        for path in paths:
            for extension in self.__image_extensions:
                for image_path in glob.glob(os.path.join(path, extension)):
                    with Image.open(image_path) as img:
                        image_name = os.path.splitext(os.path.basename(image_path))[0]
                        new_image_path = os.path.join(self.__dataset_path, f"{image_name}.png")
                        img.convert("RGB").save(new_image_path, "PNG")
                        self.__images.append(f"{image_name}.png")
    
    def __clear_dataset(self) -> None:
        for file_name in os.listdir(self.__dataset_path):
            file_path = os.path.join(self.__dataset_path, file_name)
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")
