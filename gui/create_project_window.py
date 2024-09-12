import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize, Qt
from utils.project_manager import ProjectManager

class NewProjectWindow(QMainWindow):
    pass

class NewProjectWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("New Project")
        self.setGeometry(100, 100, 400, 250)
    
        main_layout = QVBoxLayout()

        # Heading
        heading_label = QLabel("Create New Project")
        heading_font = QFont()
        heading_font.setBold(True)
        heading_font.setPointSize(16)
        heading_label.setFont(heading_font)
        heading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(heading_label)

        # Project Name input
        project_name_layout = QHBoxLayout()
        project_name_label = QLabel("Project Name:")
        self.project_name_input = QLineEdit()
        self.project_name_input.textChanged.connect(self.update_initialization_path)
        project_name_layout.addWidget(project_name_label)
        project_name_layout.addWidget(self.project_name_input)
        main_layout.addLayout(project_name_layout)

        # Path input
        path_layout = QHBoxLayout()
        path_label = QLabel("Path:")
        self.path_input = QLineEdit()
        self.path_input.textChanged.connect(self.update_initialization_path)
        self.browse_button = QPushButton()
        self.browse_button.setIcon(QIcon.fromTheme("folder"))
        self.browse_button.setIconSize(QSize(24, 24))
        self.browse_button.setFixedSize(30, 30)
        self.browse_button.clicked.connect(self.select_directory)

        # Add the layout
        path_layout.addWidget(path_label)
        path_layout.addWidget(self.path_input)
        path_layout.addWidget(self.browse_button)
        main_layout.addLayout(path_layout)

        # Dynamic label for showing the initialization path
        self.init_path_label = QLabel("The project will be initialized in /")
        main_layout.addWidget(self.init_path_label)

        # Action buttons
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.create_button = QPushButton("Create Project")
        self.cancel_button = QPushButton("Cancel")

        self.create_button.clicked.connect(self.create_project)
        self.cancel_button.clicked.connect(self.cancel_project)

        button_layout.addWidget(self.create_button)
        button_layout.addWidget(self.cancel_button)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
    
    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Project Directory")
        if directory:
            self.path_input.setText(directory)
    
    def create_project(self):
        project_name = self.project_name_input.text()
        project_path = self.path_input.text()
        
        if project_name and project_path:
            ProjectManager.create_project(project_path, project_name)
        else:
            print("Please enter a valid project name and path.")
    
    def cancel_project(self):
        self.reject()
    
    def update_initialization_path(self):
        project_name = self.project_name_input.text()
        project_path = self.path_input.text()
        
        if project_path and project_name:
            self.init_path_label.setText(f"The project will be initialized in {project_path}/{project_name}")
        elif project_path:
            self.init_path_label.setText(f"The project will be initialized in {project_path}/")
        else:
            self.init_path_label.setText("Project does not have a path")
