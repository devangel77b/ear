#!/bin/env python

class Vertex(object):
    def __init__(self,x=None):
        self.x = None
        return

class HalfEdge(object):
    def __init__(self):
        self.v = None
        self.f = None
        self.nexth = None
        self.twinh = None
        return

class Edge(object):
    def __init__(self,uv=None,assignment=None):
        self.h = None
        self.assignment = assignment
        return

class Face(object):
    def __init__(self,h=None):
        self.h = h
        return

class GenericHEDS(object):
    def __init__(self):
        self.vertices = None
        self.edges = None
        self.faces = None
        return
    
class CreasePattern(GenericHEDS):
    def __init__(self):
        super.__init__(self)
        return
    
    


    


        

    
