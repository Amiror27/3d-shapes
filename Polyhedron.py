import numpy as np
from Ray import Ray

class Polyhedron:
    def __init__(self, vertices, facemap):
        self.vertices = vertices
        self.facemap = facemap
    
    def __repr__(self):
        return str([f"{i}: {self.vertices[i]}" for face in self.facemap for i in face])
    
    @property
    def z_order(self):
        return np.argsort([np.mean([self.vertices[i, 2] for i in face]) for face in self.facemap])
    
    @property
    def center_of_mass(self):
        return np.mean(self.vertices, axis = 0)
    
    def face(self, index):
        return np.array([self.vertices[i] for i in self.facemap[index]])
    
    def rotate(self, matrix):
        self.vertices = self.center_of_mass + (matrix@(self.vertices-self.center_of_mass).T).T

    def project_face(self, index):
        vertices = self.face(index)
        projected_vertices = np.empty(shape=(vertices.shape[0], 2))
        projected_vertices[:, 0] = vertices[:, 0] * 2**(vertices[:, 2] * 1e-3)
        projected_vertices[:, 1] = vertices[:, 1] * 2**(vertices[:, 2] * 1e-3)
        return projected_vertices
    