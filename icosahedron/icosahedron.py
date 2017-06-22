"""Subdivided icosahedral mesh generation"""
from __future__ import print_function
import numpy as np

# following: http://blog.andreaskahler.com/2009/06/creating-icosphere-mesh-in-code.html
# hierarchy:
# mesh -> triangle -> point

class point:
    """A 3D point on the mesh"""
    def __init__(self, x, y, z):
        self.coords = np.array([x, y, z])
        
class triangle:
    """A triangle containing three adjacent points"""
    def __init__(self, p0, p1, p2):
        self.points = [p0, p1, p2] 
              
def icosahedron:
    """Establish the base icosahedron"""
    # golden ration
    t = (1.0 + np.sqrt(5.0)) / 2.0
    
    # generate vertices
    # vertices are points
    verts = []
    #
    verts.append(point(-1, t, 0))
    verts.append(point( 1, t, 0))
    verts.append(point(-1,-t, 0))
    verts.append(point( 1,-t, 0))
    #
    verts.append(point( 0,-1, t))
    verts.append(point( 0, 1, t))
    verts.append(point( 0,-1,-t))
    verts.append(point( 0,-1,-t))
    #
    verts.append(point( t, 0,-1))
    verts.append(point( t, 0, 1))
    verts.append(point(-t, 0,-1))
    verts.append(point(-t, 0, 1))
    
    # collect vertices into triangles
    tris = []
    # 5 faces around point 0
    tris.append( triangle( verts[0],verts[11],verts[5]))
    tris.append( triangle( verts[0],verts[5],verts[1]))
    tris.append( triangle( verts[0],verts[1],verts[7]))
    tris.append( triangle( verts[0],verts[7],verts[10]))
    tris.append( triangle( verts[0],verts[10],verts[11]))
    # 5 adjacent faces
    tris.append( triangle( verts[1],verts[5],verts[9]))
    tris.append( triangle( verts[5],verts[11],verts[14]))
    tris.append( triangle( verts[11],verts[10],verts[2]))
    tris.append( triangle( verts[10],verts[7],verts[6]))
    tris.append( triangle( verts[7],verts[1],verts[8]))
    # 5 faces around point 3
    tris.append( triangle( verts[3],verts[9],verts[4]))
    tris.append( triangle( verts[3],verts[4],verts[2]))
    tris.append( triangle( verts[3],verts[2],verts[6]))
    tris.append( triangle( verts[3],verts[6],verts[8]))
    tris.append( triangle( verts[3],verts[8],verts[9]))
    # 5 adjacent faces
    tris.append( triangle( verts[4],verts[9],verts[5]))
    tris.append( triangle( verts[2],verts[4],verts[11]))
    tris.append( triangle( verts[6],verts[2],verts[10]))
    tris.append( triangle( verts[8],verts[6],verts[7]))
    tris.append( triangle( verts[9],verts[8],verts[1]))
    
    return tris
    
def