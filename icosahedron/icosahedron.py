"""Subdivided icosahedral mesh generation"""
from __future__ import print_function
import numpy as np

# following: http://blog.andreaskahler.com/2009/06/creating-icosphere-mesh-in-code.html
# hierarchy:
# Icosphere -> Triangle -> Point

class IcoSphere(level):
    """A collection of triangles"""
    
    # maximum level for subdivision of the icosahedron
    maxlevel = 8
     
    def __init__(self, level):       
        if type(level) is not int:
            raise TypeError('level must be an integer')
        else if level > maxlevel:
            raise Exception('level must be no larger than ' + str(maxlevel))
        
        self.level = level
        
        # initialise level 0 icosahedron
        self.triangles = icosahedron()
        
        # refine triangles
        for l in range(self.level):
            faces = []
            for tri in self.triangles:
                # replace triangle by 4 triangles
                p = tri.pts
                p.append(_getMiddlePoint( tri.pts[0], tri.pts[1]))
                p.append(_getMiddlePoint( tri.pts[0], tri.pts[2]))
                p.append(_getMiddlePoint( tri.pts[1], tri.pts[2]))
                faces.append( Triangle( p[0], p[3], p[5]))
                faces.append( Triangle( p[1], p[4], p[3]))
                faces.append( Triangle( p[2], p[5], p[4]))
                faces.append( Triangle( p[3], p[4], p[5]))
            self.triangles = faces
        
    class Triangle:
        """A triangle adjoining three adjacent points"""
        def __init__(self, pts):              
            if isinstance(pts, list):
                self.pts = pts
            else:
                raise TypeError('pts must be a list')

    class Point:
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
        """Dictionary of middle points"""
        def __init__(self):
            return {}

        

        
    def _getMiddlePoint(p1, p2):
        """return Point"""
        if not isinstance(p1,Point) or not isinstance(p2,Point):
            raise TypeError('p1 and p2 must be Points')
        
        
                
def icosahedron():
    """Establish the base icosahedron"""
    # golden ration
    t = (1.0 + np.sqrt(5.0)) / 2.0
    
    # generate vertices
    # vertices are Points
    verts = []
    verts.append(Point( 0, np.array([-1, t, 0])))
    verts.append(Point( 1, np.array([ 1, t, 0])))
    verts.append(Point( 2, np.array([-1,-t, 0])))
    verts.append(Point( 3, np.array([ 1,-t, 0])))
    verts.append(Point( 4, np.array([ 0,-1, t])))
    verts.append(Point( 5, np.array([ 0, 1, t])))
    verts.append(Point( 6, np.array([ 0,-1,-t])))
    verts.append(Point( 7, np.array([ 0,-1,-t])))
    verts.append(Point( 8, np.array([ t, 0,-1])))
    verts.append(Point( 9, np.array([ t, 0, 1])))
    verts.append(Point(10, np.array([-t, 0,-1])))
    verts.append(Point(11, np.array([-t, 0, 1])))
    
    # collect vertices into triangles
    tris = []
    # 5 faces around point 0
    tris.append( Triangle([ verts[0],verts[11], verts[5]] ))
    tris.append( Triangle([ verts[0], verts[5], verts[1]] ))
    tris.append( Triangle([ verts[0], verts[1], verts[7]] ))
    tris.append( Triangle([ verts[0], verts[7],verts[10]] ))
    tris.append( Triangle([ verts[0],verts[10],verts[11]] ))
    # 5 adjacent faces
    tris.append( Triangle([ verts[1], verts[5], verts[9]] ))
    tris.append( Triangle([ verts[5],verts[11],verts[14]] ))
    tris.append( Triangle([verts[11],verts[10], verts[2]] ))
    tris.append( Triangle([verts[10], verts[7], verts[6]] ))
    tris.append( Triangle([ verts[7], verts[1], verts[8]] ))
    # 5 faces around point 3
    tris.append( Triangle([ verts[3], verts[9], verts[4]] ))
    tris.append( Triangle([ verts[3], verts[4], verts[2]] ))
    tris.append( Triangle([ verts[3], verts[2], verts[6]] ))
    tris.append( Triangle([ verts[3], verts[6], verts[8]] ))
    tris.append( Triangle([ verts[3], verts[8], verts[9]] ))
    # 5 adjacent faces
    tris.append( Triangle([ verts[4], verts[9], verts[5]] ))
    tris.append( Triangle([ verts[2], verts[4],verts[11]] ))
    tris.append( Triangle([ verts[6], verts[2],verts[10]] ))
    tris.append( Triangle([ verts[8], verts[6], verts[7]] ))
    tris.append( Triangle([ verts[9], verts[8], verts[1]] ))
    
    return tris
    
def refine_triangle:
    
    