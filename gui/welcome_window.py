from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QApplication, QVBoxLayout, QHBoxLayout, QToolButton,
    QLabel, QMessageBox, QFileDialog
)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize, Qt

from gui.create_project_window import NewProjectWindow

class WelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome to Image Labeler")
        self.setFixedSize(600, 400)
        self.setCentralWidget(WelcomeWidget())

class WelcomeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.new_project_window = None

        # Main layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Heading and description text
        heading_label = QLabel("Image labeler")
        heading_font = QFont("Arial", 20, QFont.Weight.Bold)
        heading_label.setFont(heading_font)
        heading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(heading_label)

        description_label = QLabel(
            "Create a new project to start from scratch.\n"
            "Open existing project from disk or version control."
        )
        description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(description_label)

        # Buttons layout
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Open Project Button
        open_button = QToolButton()
        open_button.setText("Open")
        open_button.setIcon(QIcon.fromTheme("folder"))
        open_button.setIconSize(QSize(48, 48))
        open_button.setFixedSize(140, 140)
        open_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        open_button.clicked.connect(self.open_project)
        button_layout.addWidget(open_button)

        # New Project Button
        new_button = QToolButton()
        new_button.setText("New Project")
        new_button.setIcon(QIcon.fromTheme("list-add"))
        new_button.setIconSize(QSize(48, 48))
        new_button.setFixedSize(140, 140)
        new_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        new_button.clicked.connect(self.new_project)
        button_layout.addWidget(new_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def open_project(self):
        project_dir = QFileDialog.getExistingDirectory(self, "Select Project Directory")
        if project_dir:
            QMessageBox.information(self, "Project Opened", f"Opened project at: {project_dir}")
        else:
            QMessageBox.warning(self, "Open Project", "No directory selected.")

    def open_project_window(self) -> None:
        pass

    def new_project(self):
        if self.new_project_window is None:
            self.new_project_window = NewProjectWindow()
            
        self.new_project_window.show()

def initialize():
    window = WelcomeWindow()
    window.show()
