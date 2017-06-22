"""Subdivided icosahedral mesh generation"""
from __future__ import print_function
import numpy as np

# hierarchy:
# mesh -> triangle -> vertex -> point

class point:
    """A point on the mesh"""
    def __init__(self):
        self.id
        self.level
        self.coords = 
        self.

class vertex:
    """A line joining adjacent points"""
    def __init__(self):
        self.id
        self.midpoint
        self.points = []
        
class triangle:
    """A triangle containing three vertices and three points"""
    def __init__(self):
        self.id
        self.vertices = []
        

class mesh:
    """A mesh built up of triangles"""
    def __init__(self):
        self.id
        
