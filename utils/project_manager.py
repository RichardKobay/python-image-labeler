import os
import json
import sys
from gui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication


class ProjectManager():
    def __init__(self) -> None:
        self.projects = ProjectModelJSON()
        self.settings_json = self.get_settings_file()
    
    def get_settings_file(self) -> str:
        home_directory = os.path.expanduser('~')
        settings_directory = os.path.join(home_directory, '.imglblr')
        return os.path.join(settings_directory, 'app-settings.json')
    
    def has_projects(self) -> bool:
        return len(self.projects.projects) > 0
    
    def load_projects(self) -> None:
        with open(self.settings_json, 'r') as file:
            data = json.load(file)
            projects_data = data.get('projects', [])
            self.projects = ProjectModelJSON([ProjectModel(p['id'], p['path']) for p in projects_data])
    
    def add_project_to_json(self, project_path: str) -> None:
        if self.project_exists(project_path):
            return

        if self.projects.projects:
            new_id = self.projects.projects[-1].id + 1
        else:
            new_id = 1

        new_project = ProjectModel(new_id, project_path)
        self.projects.projects.append(new_project)
        self.save_projects_to_json()
    
    def save_projects_to_json(self) -> None:
        projects_data = [{'id': p.id, 'path': p.path} for p in self.projects.projects]
        data = {'projects': projects_data}

        with open(self.settings_json, 'w') as file:
            json.dump(data, file, indent=4)
    
    
    
    def project_exists(self, project_path: str) -> None:
        for project_model in self.projects.projects:
            if project_model.path == project_path:
                return True
        
        return False
    
    @staticmethod
    def open_project(project_path: str) -> None:
        project_manager = ProjectManager()
        window = MainWindow(project_path)
        window.show()
        project_manager.add_project_to_json(project_path)
    
    @staticmethod
    def create_project(project_path: str, project_name: str) -> None:
        if project_name and project_path:
            project_path = f'{project_path}/{project_name}'
            if os.path.exists(project_path):
                print('The directory is not empty')
                return
            ProjectManager.initialize_project_folder(project_path)
            ProjectManager.create_project_files(project_path)
            ProjectManager.open_project(project_path)
        else:
            print("Please enter a valid project name and path.")
    
    @staticmethod
    def initialize_project_folder(project_path: str) -> None:
        os.makedirs(project_path)
        os.makedirs(f'{project_path}/.imglblr')
        os.makedirs(f'{project_path}/dataset')
        os.makedirs(f'{project_path}/exported-data')
        os.makedirs(f'{project_path}/polygon-data')
        print('Project created successfully')
    
    @staticmethod
    def create_project_files(project_path: str) -> None:
        project_settings_path = os.path.join(project_path, '.imglblr', 'project-setting.json')
        polygon_json_path = os.path.join(project_path, 'polygon-data', 'polygons.json')

        os.makedirs(os.path.dirname(project_settings_path), exist_ok=True)
        os.makedirs(os.path.dirname(polygon_json_path), exist_ok=True)

        if not os.path.isfile(project_settings_path):
            try:
                with open(project_settings_path, 'w') as file:
                    file.write('{}')
            except Exception as e:
                print(f'Could not create project settings file: {e}')

        if not os.path.isfile(polygon_json_path):
            try:
                with open(polygon_json_path, 'w') as file:
                    file.write('{}')
            except Exception as e:
                print(f'Could not create polygon data file: {e}')
    
    @staticmethod
    def open_all_projects() -> None:
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
        app.main_windows = []  # A list to store references to all opened main windows
        
        project_manager = ProjectManager()
        for project in project_manager.projects.projects:
            main_window = MainWindow(project.path)
            app.main_windows.append(main_window)
            main_window.show()

class ProjectModelJSON():
    def __init__(self, projects: list = None) -> None:
        self.projects = projects if projects else []

class ProjectModel():
    def __init__(self, id: int, path: str) -> None:
        self.id = id
        self.path = path
