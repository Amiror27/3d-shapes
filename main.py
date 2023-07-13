import numpy as np
import pygame as pg
from Ray import Ray
from Polyhedron import Polyhedron


#screen dimensions
SW = 1200 #screen width
SH = 900 #screen height
CZ = 1000 #camera plain, maximum z
#minimum z = -1000

tetrahedron_vertices = np.array([[0,115, 0], [100, -58, 0], [-100, -58, 0], [0,0,167]])
hexahedron_vertices = np.array([[-100, -100, -100], [100, -100, -100], [100, -100, 100], [-100, -100, 100], [-100, 100, -100], [100, 100, -100], [100, 100, 100], [-100, 100, 100]])

tetrahedron_facemap = ((0,1,2), (0,1,3), (0,2,3), (1,2,3))
hexahedron_facemap = ((0,1,2,3), (0,1,5,4), (0,3,7,4), (6,5,4,7), (6,5,1,2), (6,7,3,2))

vel = 5
lightsource = (-500,500,500)
camera = (0,0,1000)

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255, 255, 0)
magenta = (255,0,255)
cyan = (0,255, 255)
grey = (127, 127, 127)
colors = [red, green, blue, yellow, magenta, cyan]

#utility functions
def rad(a):
    return a * np.pi / 180

def to_pixel(vertices):
    new_vertices = np.empty(shape=[vertices.shape[0], 2])
    new_vertices[:, 0] = vertices[:, 0]+(SW/2)
    new_vertices[:, 1] = vertices[:, 1]+(SH/2)
    return new_vertices

#rotation functions
def rot_matrix_x(a): #yz plane
    return np.array([[1,0,0], [0, np.cos(a), np.sin(a)], [0, -np.sin(a), np.cos(a)]])


def rot_matrix_y(a): #xz plane
    return np.array([[np.cos(a), 0, -np.sin(a)], [0,1,0], [np.sin(a), 0, np.cos(a)]])


def rot_matrix_z(a): #xy plane
    return np.array([[np.cos(a), np.sin(a), 0], [-np.sin(a), np.cos(a), 0], [0,0,1]])

#graphics functions
def draw_solid_ph(ph):
    for i in ph.z_order:
        pg.draw.polygon(screen, colors[i], to_pixel(ph.project_face(i)).tolist())

def draw_base():
    screen.fill(white)

pol2 = Polyhedron(tetrahedron_vertices, tetrahedron_facemap)

# pygame setup
pg.init()
screen = pg.display.set_mode((SW, SH))

clock = pg.time.Clock()
running = True
pg.display.set_caption('')
angle = rad(1.5)

#main pygame loop
while running:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
    keys = pg.key.get_pressed()
    if keys[pg.K_s]:
        pol2.rotate(rot_matrix_x(angle))
    if keys[pg.K_w]:
        pol2.rotate(rot_matrix_x(-angle))
    if keys[pg.K_a]:
        pol2.rotate(rot_matrix_y(angle))
    if keys[pg.K_d]:
        pol2.rotate(rot_matrix_y(-angle))
    if keys[pg.K_q]:
        pol2.rotate(rot_matrix_z(angle))
    if keys[pg.K_e]:
        pol2.rotate(rot_matrix_z(-angle))

    draw_base()
    draw_solid_ph(pol2)
    pg.display.update()
    
pg.quit()
