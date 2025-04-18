#!/bin/env python

class Vertex():
    def __init__(self,x=None):
        self.x = None
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
        self.vertices = None
        self.edges = None
        self.faces = None
        return
    
    


    


        

    
