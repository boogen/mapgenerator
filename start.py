import sys, os, mapgenerator
from PyQt4 import QtGui, QtCore



class MapWidget(QtGui.QWidget):
    
    def __init__(self, map):
        super(MapWidget, self).__init__()
        self.map = map
        self.initUI()

    def initUI(self):
        
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                
                if self.map[i][j] == 1:
                    image = "Wall.png"
                elif self.map[i][j] == 0:
                    image = "Ground.png"

                path = os.path.join("assets", image)
                pixmap = QtGui.QPixmap(path).scaled(32, 32)
                l1 = QtGui.QLabel(self)
                l1.setPixmap(pixmap)
                l1.move(j * 32, i * 30)


class MainWidget(QtGui.QWidget):
    
    def __init__(self, map):
        super(MainWidget, self).__init__()

        self.initUI(map)

    def initUI(self, map):

        self.mapWidget = MapWidget(map)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.mapWidget)
        self.setLayout(hbox)
        self.setGeometry(0, 0, 1024, 768)
        self.move(100, 100)
        self.setWindowTitle('Map Generator, CodeName: BAD ASS HEROES')
        self.show()


    def mousePressEvent(self, event):
        self.pressed = True
        self.diff = (self.mapWidget.x() - event.x(), self.mapWidget.y() - event.y())


    def mouseReleaseEvent(self, event):
        self.pressed = False

    def mouseMoveEvent(self, event):
        if self.pressed:
            self.mapWidget.move(event.x() + self.diff[0], event.y() + self.diff[1])
            self.mapWidget.update(0, 0, 1024, 1024)
            slef.mapWidget.repaint()

def main():
    mapgen = mapgenerator.MapGenerator(16)
    app = QtGui.QApplication(sys.argv)
    es = MainWidget(mapgen.getMap())
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
