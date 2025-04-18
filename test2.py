#!/bin/env python

import json

class CreasePattern(object):
    def __init__(self):
        self.json
        self.vertices_coords = None
        self.edges_vertices = None
        self.edges_assignment = None
        self.faces_vertices = None
        return

    @classmethod
    def from_fold(cls,filename):
        handle = open(filename,'r')
        fold_dict = json.load(handle)
        handle.close()
        result = cls()
        result.vertices_coords = fold_dict['vertices_coords']
        result.edges_vertices = fold_dict['edges_vertices']
        result.edges_assignment = fold_dict['edges_assignment']
        result.faces_vertices = fold_dict['faces_vertices']
        return result

    def as_fold(self):
        return
