#!/bin/env python

import json
import drawsvg

# file metadata
FM = dict()
FM['file_spec'] = 1
FM['file_creator'] = "Python 3.13"
FM['file_author'] = "Dennis Evangelista"
FM['file_classes'] = ["singleModel"] 




G = dict()

# frame metadata
G['frame_title'] = "crane cp"
G['frame_classes'] = ["creasePattern"]
G['frame_attributes'] = ["2D"]
G['frame_unit'] = "unit" #in, pt, m, cm, mm, um, nm

# actual mesh geometry and topology data
G['vertices_coords']=[[0,1],[1,1],[1,0],[0,0],[0.5,0.5],[0.5,0.207106781187],[0.207106781187,0.5],[0.5,0.792893218813],[0.792893218813,0.5],[0.66591068104,0.5],[0.716772751325,0.423879532511],[0.865619448968,0.324423348821],[0.5,0.66591068104],[0.423879532511,0.716772751325],[0.324423348821,0.865619448968],[0.5,0.33408931896],[0.576120467489,0.283227248675],[0.675576651179,0.134380551032],[0.33408931896,0.5],[0.283227248675,0.576120467489],[0.134380551032,0.675576651179],[0.5,0],[0.5,1],[0.476712746783,0.094824061023],[0.523287253217,0.905175938977],[0.461939766256,0.191341716183],[0.404137552497,0.27003607936],[0.353553390593,0.353553390593],[0.27003607936,0.404137552497],[0.191341716183,0.461939766256],[0.094824061023,0.476712746783],[0,0.5],[0.538060233744,0.808658283817],[0.595862447503,0.72996392064],[0.646446609407,0.646446609407],[0.72996392064,0.595862447503],[0.808658283817,0.538060233744],[0.905175938977,0.523287253217],[1,0.5],[0.373017462227,0.792893218813],[0.207106781187,0.626982537773],[0.180807836521,0.563491268887],[0.117316567635,0.589790213552],[0,0.589790213552],[0.436508731113,0.819192163479],[0.410209786448,0.882683432365],[0.410209786448,1],[0.180807836521,0],[0.150809885227,0.029997951295],[0.16704465948,0.069192163479],[0.127850447296,0.08542693773200005],[0.127850447296,0.127850447296],[0.085426937732,0.127850447296],[0.069192163479,0.16704465948],[0.029997951295,0.150809885227],[0,0.180807836521]]
G['faces_vertices']=[[10,11,8],[37,36,8,11],[10,8,9],[36,35,9,8],[4,15,16,10,9],[16,17,2,11,10],[7,13,12],[19,18,4,12,13],[33,32,7,12],[34,33,12,4],[25,23,17,5],[16,5,17],[27,26,15,4],[5,16,15],[43,42,20,0],[40,39,14,0,20],[29,28,18,6],[19,6,18],[24,1,22],[45,46,0,14],[17,23,21,2],[48,47,21,23],[28,27,4,18],[46,45,24,22],[32,1,24],[35,34,4,9],[51,50,26,27],[52,51,27,28],[53,52,28,29],[42,43,31,30],[55,54,30,31],[41,42,30,29,6],[25,5,15,26],[45,44,7,32,24],[1,32,33],[1,33,34],[1,34,35],[1,35,36],[1,36,37],[11,2,38,37],[1,37,38],[44,39,13,7],[44,14,39],[40,19,13,39],[41,40,20],[41,6,19,40],[20,42,41],[45,14,44],[49,48,23,25],[50,49,25,26],[48,3,47],[54,53,29,30],[3,49,50],[3,50,51],[3,51,52],[3,52,53],[3,53,54],[3,54,55],[48,49,3]]
G['edges_vertices']=[[8,11],[9,8],[9,10],[10,11],[10,8],[12,13],[7,12],[12,4],[5,17],[4,15],[15,16],[0,20],[6,18],[18,19],[22,1],[0,14],[21,2],[21,23],[18,4],[22,24],[24,1],[4,9],[16,10],[26,27],[27,28],[28,29],[30,31],[29,6],[28,18],[27,4],[26,15],[25,5],[24,32],[32,33],[33,34],[34,35],[35,36],[36,37],[37,38],[1,38],[8,36],[36,1],[11,37],[37,1],[9,35],[35,1],[7,32],[32,1],[12,33],[33,1],[4,34],[34,1],[13,7],[14,39],[39,13],[19,13],[20,40],[40,19],[6,19],[40,39],[40,41],[41,42],[20,41],[41,6],[30,42],[42,20],[42,43],[0,43],[43,31],[0,46],[46,22],[39,44],[14,44],[44,7],[45,46],[44,45],[14,45],[45,24],[38,2],[23,25],[17,23],[2,17],[2,11],[25,26],[5,15],[16,5],[17,16],[3,47],[47,21],[30,29],[23,48],[49,50],[50,51],[51,52],[52,53],[53,54],[54,55],[31,55],[55,3],[3,54],[54,30],[3,49],[49,25],[3,53],[53,29],[3,52],[52,28],[3,51],[51,27],[3,50],[50,26],[47,48],[48,49],[3,48]]
G['edges_assignment']=["M","M","V","M","V","V","M","M","M","M","V","M","M","V","B","M","B","M","M","M","V","M","V","V","V","M","M","M","M","V","M","M","V","M","V","V","M","V","M","B","M","M","V","V","M","M","M","M","M","M","V","M","V","M","M","V","M","M","V","M","V","M","M","M","V","V","V","B","B","B","B","V","M","M","V","M","V","V","B","V","V","M","M","M","M","V","M","B","B","V","V","V","M","M","V","M","V","B","B","V","V","M","M","M","M","M","M","V","M","M","M","V","M","V"]

# output as a FOLD file, e.g. json 
with open("test4.fold",'w') as handle:
    json.dump(FM | G, handle)
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
D.save_svg('test4.svg')
#D.save_png('test4.png')
