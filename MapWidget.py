import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class MapWidget(QWidget):

    def __init__(self, map):
        QWidget.__init__(self)
        self.map = map
        self.blockSize = 32
        path = os.path.join("assets", "Wall.png")
        self.wall = QImage(path).scaled(self.blockSize, self.blockSize)
        path = os.path.join("assets", "Ground.png")
        self.ground = QImage(path).scaled(self.blockSize, self.blockSize)
        self.setUpdatesEnabled(True)

    def setSize(self, width, height):
        self._width = width
        self._height = height
        self.setGeometry(0, 0, self._width, self._height)

    def setMap(self, map):
        self.map = map
        self.setPosition(0, 0)
        self.repaint()
        
    def mousePressEvent(self, event):
        self.emit(SIGNAL("mousePressed"), event)

    def setPosition(self, posX, posY):
        mapWidth = len(self.map[0]) * self.blockSize
        mapHeight = len(self.map) * self.blockSize
        if mapWidth < self._width:
            posX = 0
        elif posX < -mapWidth + self._width:
            posX = -mapWidth + self._width
        elif posX > 0:
            posX = 0

        if mapHeight < self._height:
            posY = 0
        elif posY < -mapHeight + self._height and mapHeight > self._height:
            posY = -mapHeight + self._height
        elif posY > 0:
            posY = 0

        self.setGeometry(posX, posY, self._width - posX, self._height - posY)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)       
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                
                if self.map[i][j] == 1:
                    painter.drawImage(QPoint(i * 32, j * 32), self.wall)
                elif self.map[i][j] == 0:
                    painter.drawImage(QPoint(i * 32, j * 32), self.ground)
        painter.end()
