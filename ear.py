#!/bin/env python

import json

class Vertex(object):
    def __init__(self,x=None):
        self.x = x
        self.index = None
        return
    
class Edge(object):
    def __init__(self):
        self.vertices = None
        self.assignment = None
        self.index = None
        return

class Face(object):
    def __init__(self):
        self.edges = None
        self.index = None
        return

class Surface(object):
    def __init__(self):
        self.vertices = list()
        self.edges = list()
        self.faces = list()
        return
    
    def add_vertex(self,x):
        result = Vertex(x)
        self.vertices.append(result)
        result.index = self.vertices.index(result)
        return result

    def add_edge_by_indices(self,v):
        result = Edge()
        result.vertices = v
        self.edges.append(result)
        result.index = self.edges.index(result)
        return result
    
    def add_face_by_indices(self,v):
        result = Face()
        result.vertices = v
        self.faces.append(result)
        result.index = self.faces.index(result)
        return result
    
    def as_dict(self):
        result = dict()
        result['vertices_coords']=list()
        for v in self.vertices:
            result['vertices_coords'].append(v.x)
        result['edges_vertices']=list()
        for e in self.edges:
            result['edges_vertices'].append(e.vertices)
        result['faces_vertices']=list()
        for f in self.faces:
            result['faces_vertices'].append(f.vertices)
        return result




        


def from_fold(filename):
    handle = open(filename,'r')
    json_dict = json.load(handle)
    handle.close()
    result = Surface()
    for v in json_dict['vertices_coords']:
        result.add_vertex(v)
    for e in json_dict['edges_vertices']:
        result.add_edge_by_indices(e)
    for f in json_dict['faces_vertices']:
        result.add_face_by_indices(f)
    return result

    
    
    


    


        

    
