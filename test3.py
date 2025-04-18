#!/bin/env python

import json
import drawsvg

# file metadata
FM = dict()
FM['file_spec'] = 1
FM['file_creator'] = "Python 3.13"
FM['file_author'] = "Dennis Evangelista"
#FM['file_title'] = "title"
#FM['file_description'] = "description"
FM['file_classes'] = ["singleModel"] # also multiModel, animation, diagrams 





G = dict()

# frame metadata
#G['frame_author'] = "author"
G['frame_title'] = "title"
#G['frame_description'] = "description"
G['frame_classes'] = ["creasePattern"] # foldedForm, graph, linkages
G['frame_attributes'] = ["2D"] # also 3D, abstract, manifold/nonManifold, orientable/nonOrientable,selfTOuching/nonSelfTouching,selfIntersecting/nonselfINtersecting,cuts/noCuts,joins/noJOins,convexFaces/nonConvexFaces...
G['frame_unit'] = "unit" #in, pt, m, cm, mm, um, nm

# actual mesh geometry and topology data
G['vertices_coords'] = [[0,0],[1,0],[1,1],[0,1]]
G['edges_vertices'] = [[0,1],[1,2],[2,3],[3,0],[0,2]]
G['edges_assignment'] = ['B','B','B','B','M']
G['faces_vertices'] = [[0,1,2],[2,3,0]]
G['faceOrder'] = [[0,1,-1]]




# output as a FOLD file, e.g. json 
with open("test3.fold",'w') as handle:
    json.dump(FM | G, handle, indent=4)
# this part seems to work




# output as a svg
# here i am using Group to get Line for markings, scoring, or cutting
# TBD how to handle interior cuts and joins
D = drawsvg.Drawing(width=1,height=1)
reds = drawsvg.Group(id='mountain')
for i,a in enumerate(G['edges_assignment']):
    if a=="M":
        v = G['edges_vertices'][i]
        reds.append(drawsvg.Line(G['vertices_coords'][v[0]][0],
                                 G['vertices_coords'][v[0]][1],
                                 G['vertices_coords'][v[1]][0],
                                 G['vertices_coords'][v[1]][1],
                                 stroke='red',
                                 stroke_width=0.01,
                                 ))
D.append(reds)
blues = drawsvg.Group(id='valley')
for i,a in enumerate(G['edges_assignment']):
    if a=="V":
        v = G['edges_vertices'][i]
        blues.append(drawsvg.Line(G['vertices_coords'][v[0]][0],
                                  G['vertices_coords'][v[0]][1],
                                  G['vertices_coords'][v[1]][0],
                                  G['vertices_coords'][v[1]][1],
                                  stroke='blue',
                                  stroke_width=0.01,
                                  ))
D.append(blues)
scores = drawsvg.Group(id='score')
for i,a in enumerate(G['edges_assignment']):
    if a in ['M','V','F','U']:
        v = G['edges_vertices'][i]
        scores.append(drawsvg.Line(G['vertices_coords'][v[0]][0],
                                   G['vertices_coords'][v[0]][1],
                                   G['vertices_coords'][v[1]][0],
                                   G['vertices_coords'][v[1]][1],
                                   stroke='black',
                                   stroke_width=0.01,
                                   ))
D.append(scores)
cuts = drawsvg.Group(id='cut')
for i,a in enumerate(G['edges_assignment']):
    if a in ['B','C','J']:
        v = G['edges_vertices'][i]
        cuts.append(drawsvg.Line(G['vertices_coords'][v[0]][0],
                                 G['vertices_coords'][v[0]][1],
                                 G['vertices_coords'][v[1]][0],
                                 G['vertices_coords'][v[1]][1],
                                 stroke='black',
                                 stroke_width=0.01,
                                 ))
D.append(cuts)
D.set_render_size('6in','6in') # TBD need better way to do scaling
D.save_svg('test3.svg')
