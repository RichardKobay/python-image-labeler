import os
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QSplitter
from PyQt6.QtCore import Qt
from gui.components.editor.image_viewer import ImageViewer
from gui.components.bars.menu_bar.menu_bar import MenuBar

class MainWindow(QMainWindow):
    def __init__(self, project_path: str) -> None:
        super().__init__()
        self.project_path = project_path
        self.images = []
        self.__editing_mode = False
        self.init_ui()  # Initialize the UI after setting up attributes
    
    def init_ui(self) -> None:
        self.setWindowTitle('Image Labeler')

        # Create and set the MenuBar
        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Set up the main layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a QSplitter to manage resizable sidebars and central widget
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Add image viewer in the center (add other widgets as needed)
        self.image_viewer = ImageViewer(self)
        splitter.addWidget(self.image_viewer)

        # Set initial sizes for the widgets
        splitter.setSizes([200, 600])

        # Add the splitter to the layout
        layout.addWidget(splitter)

        self.setGeometry(100, 100, 1000, 600)

