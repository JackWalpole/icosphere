"""Subdivided icosahedral mesh generation"""
from __future__ import print_function
import numpy as np

# following: http://blog.andreaskahler.com/2009/06/creating-icosphere-mesh-in-code.html
# hierarchy:
# mesh -> triangle -> point

class point:
    """A 3D point on the mesh"""
    def __init__(self, id, xyz):
        if type(id) is int:
            self.id = id
        else:
            raise TypeError('id must be an integer')
            
        if not isinstance(xyz,np.ndarray):
            raise TypeError('xyz must be a numpy array')
        else if xyz.size != 3:
            raise Exception('xyz must be of size 3')
        else:
            # ensure length equals 1
            self.xyz = xyz / np.linalg.norm(xyz)

class middlePointIndexCache:
    
        
class triangle:
    """A triangle containing three adjacent points"""
    def __init__(self, id, pts):
        if type(id) is int:
            self.id = id
        else:
            raise TypeError('id must be an integer')
        
        if isinstance(pts, list):
            self.pts = pts
        else:
            raise TypeError('pts must be a list')
        
class mesh:
    """A collection of triangles""" 
    def __init__(self, triangles, level):
        self.triangles = triangles
        self.level = level
        
def getMiddlePoint():
                
def icosahedron:
    """Establish the base icosahedron"""
    # golden ration
    t = (1.0 + np.sqrt(5.0)) / 2.0
    
    # generate vertices
    # vertices are points
    verts = []
    verts.append(point( 0, np.array([-1, t, 0])))
    verts.append(point( 1, np.array([ 1, t, 0])))
    verts.append(point( 2, np.array([-1,-t, 0])))
    verts.append(point( 3, np.array([ 1,-t, 0])))
    verts.append(point( 4, np.array([ 0,-1, t])))
    verts.append(point( 5, np.array([ 0, 1, t])))
    verts.append(point( 6, np.array([ 0,-1,-t])))
    verts.append(point( 7, np.array([ 0,-1,-t])))
    verts.append(point( 8, np.array([ t, 0,-1])))
    verts.append(point( 9, np.array([ t, 0, 1])))
    verts.append(point(10, np.array([-t, 0,-1])))
    verts.append(point(11, np.array([-t, 0, 1])))
    
    # collect vertices into triangles
    tris = []
    # 5 faces around point 0
    tris.append( triangle( 0, [ verts[0],verts[11], verts[5]] ))
    tris.append( triangle( 1, [ verts[0], verts[5], verts[1]] ))
    tris.append( triangle( 2, [ verts[0], verts[1], verts[7]] ))
    tris.append( triangle( 3, [ verts[0], verts[7],verts[10]] ))
    tris.append( triangle( 4, [ verts[0],verts[10],verts[11]] ))
    # 5 adjacent faces
    tris.append( triangle( 5, [ verts[1], verts[5], verts[9]] ))
    tris.append( triangle( 6, [ verts[5],verts[11],verts[14]] ))
    tris.append( triangle( 7, [verts[11],verts[10], verts[2]] ))
    tris.append( triangle( 8, [verts[10], verts[7], verts[6]] ))
    tris.append( triangle( 9, [ verts[7], verts[1], verts[8]] ))
    # 5 faces around point 3
    tris.append( triangle(10, [ verts[3], verts[9], verts[4]] ))
    tris.append( triangle(11, [ verts[3], verts[4], verts[2]] ))
    tris.append( triangle(12, [ verts[3], verts[2], verts[6]] ))
    tris.append( triangle(13, [ verts[3], verts[6], verts[8]] ))
    tris.append( triangle(14, [ verts[3], verts[8], verts[9]] ))
    # 5 adjacent faces
    tris.append( triangle(15, [ verts[4], verts[9], verts[5]] ))
    tris.append( triangle(16, [ verts[2], verts[4],verts[11]] ))
    tris.append( triangle(17, [ verts[6], verts[2],verts[10]] ))
    tris.append( triangle(18, [ verts[8], verts[6], verts[7]] ))
    tris.append( triangle(19, [ verts[9], verts[8], verts[1]] ))
    
    return tris
    
def refine_triangle:
    
    