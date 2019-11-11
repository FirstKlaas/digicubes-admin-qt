import sys
from PyQt5 import (QtWidgets, uic)


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('uitemplates/main.ui', self) # Load the .ui file
        self.show() # Show the GUI        
        self.edLogin:QtWidgets.QLineEdit  = self.findChild(QtWidgets.QLineEdit, "edLogin")
        self.edLogin.setText("Hurra")
        
if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()