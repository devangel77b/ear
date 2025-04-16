import json
import numpy as np

class Vertex():
    def __init__(self,x=None):
        if x:
            self.x = np.array(x)
        else:
            self.x = None
        self.edges = None
        self.faces = None
        return

class Edge():
    def __init__(self,uv=None,assignment=None):
        self.assignment = assignment
        self.vertices = uv
        self.faces = None
        return

class Face():
    def __init__(self):
        self.vertices = None
        self.edges = None
        return

class CreasePattern():
    def __init__(self):
        self.json = None
        self.vertices = None
        self.edges = None
        self.faces = None
        return
    
    @classmethod
    def from_fold(cls,filename):
        handle = open(filename,'r')
        result = cls()
        result.json = json.load(handle)
        handle.close()
        
        # now unpack the vertices, edges, and faces
        result.vertices=list()
        for item in result.json['vertices_coords']:
            result.vertices.append(Vertex(x=item))
        result.edges=list()
        for item in result.json['edges_vertices']:
            result.edges.append(Edge(uv=item))
        for (index,a) in enumerate(result.json['edges_assignment']):
            result.edges[index].assignment=a
        return result
    
    


    


        

    
