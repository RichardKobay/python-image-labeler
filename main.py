import gui.welcome_window
import gui.main_window
from utils.installer import Installer
from utils.project_manager import ProjectManager
from PyQt6.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    
    project_manager = ProjectManager()
    installer = Installer()
    
    installer.install()
    project_manager.load_projects()
    
    app.main_windows = [] 
    
    if len(project_manager.projects.projects) == 0:
        app.window = gui.welcome_window.WelcomeWindow()
        app.window.show()
    else:
        for project in project_manager.projects.projects:
            print(f"Opening project: {project.path}")
            main_window = gui.main_window.MainWindow(project.path)  
            app.main_windows.append(main_window)  
            main_window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
