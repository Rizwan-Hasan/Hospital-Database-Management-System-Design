import sys

# PyQt5 Imports
from PyQt5.QtWidgets import QApplication, QStyleFactory

# noinspection PyUnresolvedReferences
import resources
# My Imports
from main import MainWindow


# Main Function ↓
def main():
	app = QApplication(sys.argv)
	app.setStyle(QStyleFactory.create('Fusion'))
	mainWindow = MainWindow()
	mainWindow.show()
	sys.exit(app.exec_())


# Start Application ↓
if __name__ == '__main__':
	main()
