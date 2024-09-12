from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QSize
import sys
from PyQt6.QtWidgets import QApplication

class ImageViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize original_pixmap to None
        self.original_pixmap = None
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.layout.addWidget(self.image_label)
    
    def load_image(self, image_path: str):
        pixmap = QPixmap(image_path)
        
        if not pixmap.isNull():
            self.original_pixmap = pixmap
            self.resize_image()
        else:
            self.image_label.setText("Failed to load image.")
    
    def resize_image(self):
        if self.original_pixmap and not self.original_pixmap.isNull():
            scaled_pixmap = self.original_pixmap.scaled(
                self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)

    def resizeEvent(self, event):
        self.resize_image()
        super().resizeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.load_image(r"C:\Users\ricar\OneDrive\Escritorio\a.png")  # Change to your image path
    viewer.resize(800, 600)
    viewer.show()
    sys.exit(app.exec())
