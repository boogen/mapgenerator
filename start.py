import sys, os, mapgenerator
from MapWidget import MapWidget
from menu import Menu
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sip

class MainWidget(QWidget):
    def __init__(self, map, width, height):
        super(MainWidget, self).__init__()
        self.width = width
        self.height = height
        self.panelWidth = 300
        self.mapSize = 16
        self.map = map
        self.initUI(self.map)
        self.setAttribute(Qt.WA_PaintUnclipped)
        self.pressed = False

    def initUI(self, map):
        self.mapWidget =None
        self.menu = None
        self.hbox = None

        self.setGeometry(0, 0, self.width, self.height)
        self.move(100, 100)
        self.setWindowTitle('Map Generator, CodeName: BAD ASS HEROES')

        self.createLayout(map)
        self.show()



    def createLayout(self, map):
        self.hbox = QHBoxLayout()
        if self.mapWidget != None:
            self.mapWidget.setParent(None)
        if self.menu:
            self.menu.setParent(None)
        else:
            self.menu = Menu(self.panelWidth, 2 * self.mapSize + 1)
        
        self.mapWidget = MapWidget(map)
        self.connect(self.mapWidget, SIGNAL("mousePressed"), self.startDragging)
        self.connect(self.menu, SIGNAL("generateMap"), self.generate)
        self.connect(self.menu, SIGNAL("newSize"), self.changeSize)
        self.connect(self.menu, SIGNAL("save"), self.save)
        self.mapWidget.setSize(self.width - self.panelWidth, self.height)
        self.hbox.addWidget(self.mapWidget)
        self.hbox.addWidget(self.menu)
        self.menu.move(self.width - self.panelWidth, 0)    
        if self.layout() != None:
            sip.delete(self.layout())
        self.setLayout(self.hbox)
        

    def changeSize(self, size):
        self.mapSize = (size - 1) / 2
        
    def generate(self):
        mapgen = mapgenerator.MapGenerator(self.mapSize)
        self.pressed = False
        self.map = mapgen.getMap()
        self.mapWidget.setMap(self.map)
        self.show()

        
    def resizeEvent(self, ev):
        self.mapWidget.setSize(ev.size().width() - self.panelWidth, ev.size().height())
        self.menu.move(ev.size().width() - self.panelWidth, 0)

    def startDragging(self, event):
        self.pressed = True
        self.diff = (-event.x(), -event.y())

    def mouseReleaseEvent(self, event):
        self.pressed = False

    def mouseMoveEvent(self, event):
        if self.pressed:
            self.mapWidget.setPosition(event.x() + self.diff[0], event.y() + self.diff[1])

    def save(self, filename):
        f = open(filename, 'w')
        f.write(str(self.mapSize * 2 + 1))
        f.write("\n")
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
#                if j > 0:
#                    f.write(",")
                f.write(str(self.map[i][j]))
            f.write("\n")

        f.close()

def main():
    mapgen = mapgenerator.MapGenerator(16)
    app = QApplication(sys.argv)    
    mw = MainWidget(mapgen.getMap(), 1024, 768)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
