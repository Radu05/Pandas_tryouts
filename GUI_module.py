from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PartlistManager")
        self.setGeometry(100, 100, 400, 300)  # (x, y, width, height)

        # Create a central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Add a label
        self.label = QLabel("Hello, PyQt6!")
        layout.addWidget(self.label)

        # Add a button
        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

    def on_button_click(self):
        self.label.setText("Button was clicked!")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()