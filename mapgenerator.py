import random, math
from sets import Set

class MapGenerator:
    
    GROUND = 0
    WALL = 1

    def __init__(self, size):
        self.block_width = 32
        self.labyrinth_size = size        
        self.createGraph()
        self.PrimsRandomSpanningTree()
        self.generateLabyrinthFromSpanningTree()
        self.offset = [0, 0]
        self.moving = False

    def createGraph(self):
        #neighborhood map
        self.graph = [[] for j in range(0, self.labyrinth_size ** 2)]
        self.edgesset = set([])
        #every node has 4 neighbours except for the borders
        for p in range(0, self.labyrinth_size ** 2):
            if p - self.labyrinth_size >= 0:
                self.graph[p].append(p - self.labyrinth_size)
                self.edgesset.add((p, p - self.labyrinth_size))
            if p + self.labyrinth_size < self.labyrinth_size ** 2:
                self.graph[p].append(p + self.labyrinth_size)
                self.edgesset.add((p, p + self.labyrinth_size))
            if p % self.labyrinth_size > 0:
                self.graph[p].append(p - 1)
                self.edgesset.add((p, p - 1))
            if p % self.labyrinth_size  < self.labyrinth_size - 1:
                self.graph[p].append(p + 1)
                self.edgesset.add((p, p + 1))
    
    def KruskalsSpanningTree(self):
        pass
            

    def PrimsRandomSpanningTree(self):
        self.edges = []
        node_list = set([0])
        

        while len(node_list) < self.labyrinth_size ** 2:
            neighbours = []
            for x in node_list:
                for y in self.graph[x]:
                    if y not in node_list:
                        neighbours.append((x, y))

            edge = neighbours[random.randint(0, len(neighbours) - 1)]
            self.edges.append(edge)
            node_list.add(edge[1])
             
    def generateLabyrinthFromSpanningTree(self):
        self.blocks_count = 2 * self.labyrinth_size + 1
        self.map = [[self.WALL for i in range(0, self.blocks_count)] for j in range(0, self.blocks_count)]

        for e in self.edges:
            #translate node id to point with two coordinates
            p1 = self.nodeToPoint(e[0])
            p2 = self.nodeToPoint(e[1])

            self.map[p1[0]][p1[1]] = self.GROUND
            self.map[p2[0]][p2[1]] = self.GROUND
            if p1[0] != p2[0]:
                self.map[min(p1[0], p2[0]) + 1][p1[1]] = self.GROUND
            if p1[1] != p2[1]:
                self.map[p1[0]][min(p1[1], p2[1]) + 1] = self.GROUND

    def nodeToPoint(self, node):
        return (2 * (node % self.labyrinth_size) + 1, int(2 * math.floor(node / self.labyrinth_size)) + 1)
    
    def positionToBlock(self, pos):
        return (int(math.floor(pos[0] / self.block_width)), int(math.floor(pos[1] / self.block_width)))

    def getMap(self):
        return self.map



             
        
