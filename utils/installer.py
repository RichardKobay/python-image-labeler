import os

class Installer():    
    def __init__(self) -> None:
        self.path = self.get_app_path()
    
    def install(self) -> None:
        if self.installed():
            return
        
        self.create_app_directory()
        self.create_json_file()
    
    def get_app_path(self) -> str:
        home_directory = os.path.expanduser('~')        
        app_path = os.path.join(home_directory, '.imglblr')        
        return app_path
    
    def app_json_exists(self) -> bool:
        return os.path.exists(os.path.join(self.path, 'app-settings.json'))
    
    def installed(self) -> bool:
        return os.path.isdir(self.path) and self.app_json_exists()
    
    def create_app_directory(self) -> None:
        if not os.path.exists(self.path):
            try:
                os.makedirs(self.path)
            except Exception as e:
                print(f"An error occurred while creating the directory: {e}")

    def create_json_file(self) -> None:
        settings_file = os.path.join(self.path, 'app-settings.json')
        if not os.path.isfile(settings_file):
            try:
                with open(settings_file, 'w') as file:
                    file.write('{\n    "projects": []\n}')
            except:
                print("There was an error creating the app settings file")
