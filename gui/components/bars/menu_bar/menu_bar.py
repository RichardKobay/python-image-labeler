from PyQt6.QtWidgets import QMenuBar, QMenu
from PyQt6.QtGui import QAction 

class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # File Menu
        file_menu = self.addMenu("File")
        new_project_action = QAction("New Project", self)
        new_project_action.triggered.connect(self.new_project_action)
        file_menu.addAction(new_project_action)

        close_project_action = QAction("Close Project", self)
        close_project_action.triggered.connect(self.close_project_action)
        file_menu.addAction(close_project_action)

        # View Menu
        view_menu = self.addMenu("View")
        self.dataset_viewer_action = QAction("Dataset Viewer", self, checkable=True)
        self.dataset_viewer_action.triggered.connect(self.toggle_dataset_viewer)
        view_menu.addAction(self.dataset_viewer_action)

        self.polygon_editor_action = QAction("Polygon Editor", self, checkable=True)
        self.polygon_editor_action.triggered.connect(self.toggle_polygon_editor)
        view_menu.addAction(self.polygon_editor_action)

        open_class_editor_action = QAction("Open Class Editor", self)
        open_class_editor_action.triggered.connect(self.open_class_editor_action)
        view_menu.addAction(open_class_editor_action)

        # Dataset Menu
        dataset_menu = self.addMenu("Dataset")
        load_dataset_action = QAction("Load Dataset", self)
        load_dataset_action.triggered.connect(self.load_dataset_action)
        dataset_menu.addAction(load_dataset_action)

        load_data_action = QAction("Load Data", self)
        load_data_action.triggered.connect(self.load_data_action)
        dataset_menu.addAction(load_data_action)

        # Polygon Editor Menu (Placeholder)
        polygon_menu = self.addMenu("Polygon Editor")
        placeholder_action = QAction("Placeholder", self)
        polygon_menu.addAction(placeholder_action)

    # Empty functions for actions
    def new_project_action(self):
        print("New Project triggered")

    def close_project_action(self):
        print("Close Project triggered")

    def toggle_dataset_viewer(self):
        print(f"Dataset Viewer toggled: {self.dataset_viewer_action.isChecked()}")

    def toggle_polygon_editor(self):
        print(f"Polygon Editor toggled: {self.polygon_editor_action.isChecked()}")

    def open_class_editor_action(self):
        print("Open Class Editor triggered")

    def load_dataset_action(self):
        print("Load Dataset triggered")

    def load_data_action(self):
        print("Load Data triggered")
