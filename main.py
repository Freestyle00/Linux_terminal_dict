from PySide2 import uic
from PySide2.QtWidgets import QApplication, QMainWindow
import webbrowser
import sys
from PySide2.QtCore import Slot

class LinuxTerminalDict():
    def run(self):
        app = QApplication(sys.argv)
        Form, Window = uic.loadUiType("UI_files/untitled.ui")
        window = MainWindow(Form, Window)
        window.Window.show()
        sys.exit(app.exec_())

class MainWindow(QMainWindow):
    def __init__(this, Form, Window):
        super(MainWindow, this).__init__()
        this.Window = Window()
        this.Form = Form()
        this.Form.setupUi(this.Window)

    @Slot()
    def on_hello_world_clicked(this):
        print("hello world")


def main():
    LinuxTerminalDict().run()


if __name__ == "__main__":
    main()
