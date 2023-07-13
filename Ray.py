import numpy as np

class Ray:
    def __init__(self, origin : np.array, direction : np.array) -> None:
        self.origin = origin #np.array
        self.direction = direction #preferably a unit vector
    

    def __repr__(self):
        return f"origin: {self.origin}, direction: {self.direction}"
    
    def segment_intersect(self, segment):
        M = np.empty(shape = (3,2))
        v = segment[1]-segment[0]
        M[:, 0] = self.direction
        M[:, 1] = -v
        t = np.linalg.pinv(M)@(segment[0]-self.origin)
        deviance = (self.origin+t[0]*self.direction)-(segment[0]+t[1]*v)
        if t[0] > 0 and 1 > t[1] > 0 and np.linalg.norm(deviance) < 1e-12:
            return self.origin + t[0]*self.direction
        return None

    def surface_intersect(self, face_vertices): #vertices are raw np array
        u = face_vertices[1]-face_vertices[0]
        v = face_vertices[2]-face_vertices[0]
        M = np.empty(shape = (3,3))
        M[:, 0] = self.direction
        M[:, 1] = -u
        M[:, 2] = -v
        t = np.linalg.inv(M)@(face_vertices[0]-self.origin)
        if t[0] > 0:
            return self.origin + t[0] * self.direction
        return None
