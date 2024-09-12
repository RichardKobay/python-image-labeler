from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class LeftBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel('Left Bar', self)
        layout.addWidget(label)
