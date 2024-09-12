import os
from pathlib import Path


class ImageModel:
    def __init__(self, image_path: str):
        self.id = ''
        self.image_path = image_path
        self.polygons = []
    
    def add_polygon(self, polygon):
        self.polygons.append(polygon)
    
    def get_polygons(self):
        return self.polygons

def load_images(path: str):
    image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"}
    images = []
    
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if Path(file_path).suffix.lower() in image_extensions:
            image_model = ImageModel(file_path)
            images.append(image_model)
    
    return images
