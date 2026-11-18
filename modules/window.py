from PyQt6.QtWidgets import QApplication, QWidget, QFrame


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather app")
        self.setGeometry(100, 100, 900, 620)
        self.setStyleSheet("background-color: black;")

        self.left_panel = QFrame(self)
        self.left_panel.setGeometry(10, 10, 275, 600)
        self.left_panel.setStyleSheet("background-color: slategray;")

        self.top_panel = QFrame(self)
        self.top_panel.setGeometry(295, 25, 595, 28)
        self.top_panel.setStyleSheet("border: 5px solid salmon;")

        self.middle_panel = QFrame(self)
        self.middle_panel.setGeometry(295, 60, 595, 235)
        self.middle_panel.setStyleSheet("border: 5px solid salmon;")

        self.bottom_panel = QFrame(self)
        self.bottom_panel.setGeometry(295, 305, 595, 290)
        self.bottom_panel.setStyleSheet("border: 5px solid salmon;")


app = QApplication([])
window = WeatherApp()
window.show()