"""Subdivided icosahedral mesh generation"""
from __future__ import print_function
import numpy as np

# following: http://blog.andreaskahler.com/2009/06/creating-icosphere-mesh-in-code.html
# hierarchy:
# Icosphere -> Triangle -> Point

class IcoSphere(level):
    """A collection of triangles and list of all points"""
    
    # maximum level for subdivision of the icosahedron
    maxlevel = 8
     
    def __init__(self, level):       
        if type(level) is not int:
            raise TypeError('level must be an integer')
        else if level > maxlevel:
            raise Exception('level must be no larger than ' + str(maxlevel))
        
        self.level = level
        self.points = []
        self.triangles = []
        
        ################################
        # initialise level 0 icosahedron
        ################################
        
        # golden ration
        t = (1.0 + np.sqrt(5.0)) / 2.0
        
        # add vertices
        _addPoint(np.array([-1, t, 0]))
        _addPoint(np.array([ 1, t, 0]))
        _addPoint(np.array([-1,-t, 0]))
        _addPoint(np.array([ 1,-t, 0]))
        _addPoint(np.array([ 0,-1, t]))
        _addPoint(np.array([ 0, 1, t]))
        _addPoint(np.array([ 0,-1,-t]))
        _addPoint(np.array([ 0,-1,-t]))
        _addPoint(np.array([ t, 0,-1]))
        _addPoint(np.array([ t, 0, 1]))
        _addPoint(np.array([-t, 0,-1]))
        _addPoint(np.array([-t, 0, 1]))
        
        # make triangles
        tris = self.triangles
        verts = self.points
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
        
        ########################################
        # refine triangles to desired mesh level
        ########################################
        
        for l in range(1, self.level):
            midPointDict = {}
            faces = []
            for tri in self.triangles:
                # replace triangle by 4 triangles
                p = tri.pts
                p.append(_getMiddlePoint( tri.pts[0], tri.pts[1], midPointDict))
                p.append(_getMiddlePoint( tri.pts[0], tri.pts[2], midPointDict))
                p.append(_getMiddlePoint( tri.pts[1], tri.pts[2], midPointDict))
                faces.append( Triangle( p[0], p[3], p[5]))
                faces.append( Triangle( p[1], p[4], p[3]))
                faces.append( Triangle( p[2], p[5], p[4]))
                faces.append( Triangle( p[3], p[4], p[5]))
            # once looped thru all triangles overwrite self.triangles
            self.triangles = faces
    
    def _addPoint(self, xyz):
        """Add point to self.points"""
        self.points.append( Point( len(self.points), xyz))
        
    def _getMiddlePoint(p1, p2, midPointDict):
        """return Point"""
        if not isinstance(p1,Point) or not isinstance(p2,Point):
            raise TypeError('p1 and p2 must be Points')        
        # does point already exist?
        key = tuple( sorted( [p1.idx, p2.idx]))
        if key in midPointDict:
            # point exists
            pass
        else:
            # point is new
            _addPoint( (p1.xyz + p2.xyz)/2)
            midPointDict[key] = self.points[-1] 
        return midPointDict[key]
        
        
class Triangle(self,pts):
    """A triangle adjoining three adjacent points"""
    def __init__(self, pts):              
        if isinstance(pts, list):
            self.pts = pts
        else:
            raise TypeError('pts must be a list')

class Point(self, idx, xyz):
    """A 3D point on the mesh"""
    def __init__(self, idx, xyz):         
        
        if type(idx) is not int:
            raise TypeError('idx must be an integer')              
        else if not isinstance(xyz,np.ndarray):
            raise TypeError('xyz must be a numpy array')
        else if xyz.size != 3:
            raise Exception('xyz must be of size 3')
        else:
            # ensure length equals 1 and add to list of points
            self.xyz = ( xyz / np.linalg.norm(xyz))
            self.idx = idx 
        

    
    