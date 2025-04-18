#!/bin/env/python

import json

class Vertex(object):
    def __init__(self,x=None):
        self.x = x # list of floats for now, numpy array later? TBD. 
        HalfEdge: self.h = None
        return

class Edge(object):
    def __init__self(self):
        HalfEdge: self.h = None
        self.edge_assignment = None
        #self.edge_foldangle = None
        #self.edge_length = None
        return

class HalfEdge(object):
    def __init__(self):
        Vertex: self.v = None
        HalfEdge: self.twinh = None
        HalfEdge: self.nexth = None
        Face: self.f = None
        return

class Face(object):
    def __init__(self):
        HalfEdge: self.h = None
        return

class GenericHEDS(objects):
    def __init__(self):
        self.vertices = None
        self.edges = None
        self.faces = None
        
        # layer data LATER
        # self.face_orders = None
        # self.edge_orders = None
        return

class CreasePattern(GenericHEDS):
    def __init__(self):
        super(self).__init__()
        return
    # from_fold
    # as_fold
    # as_svg


    

if __name__ == "__main__":

    # load a fold file
    handle = open('simple.fold','r')
    result = json.load(handle)
    handle.close()

    print("vertices: {0}".format(result['vertices_coords']))
    print("edges: {0}".format(result['edges_vertices']))
    print("faces: {0}".format(result['faces_vertices']))

    
