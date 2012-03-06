import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Menu(QWidget):

    def __init__(self, width, size):
        QWidget.__init__(self)
        self.size = size
        self.generateButton = QPushButton('Generate level', self)
        self.generateButton.setToolTip('Click me! I dare you, i double dare you.')
        self.generateButton.resize(self.generateButton.sizeHint())
        self.generateButton.move(10, 50)               
        self.generateButton.clicked.connect(self.generate)
        
        self.sizeLabel = QLabel(self)
        self.sizeLabel.setText("Sajz:")
        self.sizeLabel.move(10, 90)
        self.sizeEdit = QLineEdit(self)
        self.sizeEdit.setText(str(size))
        self.sizeEdit.textChanged[str].connect(self.onChanged)
        self.sizeEdit.move(10, 110)

        self.saveLabel = QLabel(self)
        self.saveLabel.setText("Save to file:")
        self.saveLabel.move(10, 240)
        self.saveEdit = QLineEdit(self)
        self.saveEdit.move(10, 260)


        self.saveButton = QPushButton('Save map', self)
        self.saveButton.move(10, 300)
        self.saveButton.clicked.connect(self.save)
        
        self.show()

    def save(self):
        self.emit(SIGNAL("save"), self.saveEdit.text())

    def generate(self):
        self.emit(SIGNAL("generateMap"), ())

    def onChanged(self, text):
        try:
            value = int(text)
            self.emit(SIGNAL("newSize"), int(text))
        except:
            self.sizeEdit.setText("naughty naughty")
        

    
