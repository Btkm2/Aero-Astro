# import pygame
# from pygame.locals import *
# from OpenGL.GL import *
# from OpenGL.GLU import *
# import numpy as np

# pygame.init()
# display = (800, 600)
# pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
# gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
# glTranslatef(0.0, 0.0, -10)
# glEnable(GL_DEPTH_TEST)

# def create_grid(size=20, spacing=0.5):
#     vertices = []
#     for x in range(-size, size + 1):
#         for z in range(-size, size + 1):
#             vertices.append([x * spacing, 0, z * spacing])
#     return np.array(vertices)

# def deform_grid(vertices, mass=1.0, G=0.1):
#     deformed = vertices.copy()
#     for i, vertex in enumerate(deformed):
#         x, y, z = vertex
#         r = np.sqrt(x**2 + z**2)
#         if r < 0.1: r = 0.1
#         deformed[i][1] = -G * mass / r
#     return deformed

# def draw_grid(vertices, size=20):
#     glBegin(GL_LINES)
#     glColor3f(1, 1, 1)
#     for i in range(size + 1):
#         for j in range(size):
#             idx1 = i * (size + 1) + j
#             idx2 = idx1 + 1
#             glVertex3fv(vertices[idx1])
#             glVertex3fv(vertices[idx2])
#             idx3 = j * (size + 1) + i
#             idx4 = idx3 + (size + 1)
#             glVertex3fv(vertices[idx3])
#             glVertex3fv(vertices[idx4])
#     glEnd()

# def draw_earth():
#     glPushMatrix()
#     glColor3f(0, 0, 1)  # Blue Earth
#     glTranslatef(0, 0, 0)
#     quad = gluNewQuadric()
#     gluSphere(quad, 0.5, 32, 32)
#     glPopMatrix()

# class Satellite:
#     def __init__(self, x=5, z=0):
#         self.pos = np.array([x, 0, z], dtype=float)
#         self.vel = np.array([0, 0, 0.1])

#     def update(self, grid, size=20):
#         x_idx = int((self.pos[0] + 10) / 0.5)
#         z_idx = int((self.pos[2] + 10) / 0.5)
#         idx = x_idx * (size + 1) + z_idx
#         if 0 <= idx < len(grid):
#             self.vel[1] -= 0.01 * (grid[idx][1] - self.pos[1])
#         self.pos += self.vel

#     def draw(self):
#         glPushMatrix()
#         glColor3f(1, 0, 0)  # Red satellite
#         glTranslatef(*self.pos)
#         quad = gluNewQuadric()
#         gluSphere(quad, 0.1, 16, 16)
#         glPopMatrix()

# grid = create_grid()
# deformed_grid = deform_grid(grid)
# satellite = Satellite()
# angle = 0

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()

#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glPushMatrix()
#     glRotatef(angle, 0, 1, 0)  # Rotate around Y-axis
#     draw_grid(deformed_grid)
#     draw_earth()
#     satellite.update(deformed_grid)
#     satellite.draw()
#     glPopMatrix()
    
#     angle += 1  # Slow rotation
#     pygame.display.flip()
#     pygame.time.wait(10)




# import pygame
# from pygame.locals import *
# from OpenGL.GL import *
# from OpenGL.GLU import *
# import numpy as np

# # Initialize Pygame and OpenGL
# pygame.init()
# display = (800, 600)
# pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
# glEnable(GL_DEPTH_TEST)
# glClearColor(0, 0, 0, 1)

# # Set up the camera
# gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
# glTranslatef(0, -5, -50)  # Move camera back and down to see the full grid

# # Enable lighting for 3D effect
# glEnable(GL_LIGHTING)
# glEnable(GL_LIGHT0)
# glEnable(GL_COLOR_MATERIAL)
# light_position = [0, 10, 10, 1]  # Light above and in front
# glLightfv(GL_LIGHT0, GL_POSITION, light_position)

# def create_grid(size=40, spacing=0.25):
#     vertices = []
#     for x in range(-size, size + 1):
#         for z in range(-size, size + 1):
#             vertices.append([x * spacing, 0, z * spacing])
#     return np.array(vertices)

# def deform_grid(vertices, mass=10.0, G=1.5):
#     deformed = vertices.copy()
#     for i, vertex in enumerate(deformed):
#         x, y, z = vertex
#         r = np.sqrt(x**2 + z**2)
#         if r < 0.5: r = 0.5  # Avoid extreme deformation
#         deformed[i][1] = -G * mass / (r + 1)  # Smoother falloff
#     return deformed

# def draw_grid(vertices, size=40):
#     glDisable(GL_LIGHTING)  # Disable lighting for grid lines
#     glBegin(GL_LINES)
#     glColor3f(1, 1, 1)  # White grid
#     # Draw horizontal lines (along z-axis)
#     for x in range(-size, size + 1):
#         for z in range(-size, size):
#             idx1 = (x + size) * (size * 2 + 1) + (z + size)
#             idx2 = idx1 + 1
#             if idx1 < len(vertices) and idx2 < len(vertices):
#                 glVertex3fv(vertices[idx1])
#                 glVertex3fv(vertices[idx2])
#     # Draw vertical lines (along x-axis)
#     for z in range(-size, size + 1):
#         for x in range(-size, size):
#             idx1 = (x + size) * (size * 2 + 1) + (z + size)
#             idx2 = idx1 + (size * 2 + 1)
#             if idx1 < len(vertices) and idx2 < len(vertices):
#                 glVertex3fv(vertices[idx1])
#                 glVertex3fv(vertices[idx2])
#     glEnd()
#     glEnable(GL_LIGHTING)

# def draw_earth():
#     glPushMatrix()
#     glColor3f(0, 0, 1)  # Blue Earth
#     glTranslatef(0, -10, 0)  # Move Earth below grid
#     quad = gluNewQuadric()
#     gluSphere(quad, 1.5, 32, 32)  # Larger Earth
#     glPopMatrix()

# class Satellite:
#     def __init__(self, x=8, z=0):
#         self.pos = np.array([x, 0, z], dtype=float)
#         self.vel = np.array([-0.1, 0, 0.2])  # Initial velocity with x-component for orbit

#     def update(self, grid, size=40):
#         # Adjust indices based on grid size and spacing
#         x_idx = int((self.pos[0] + (size * 0.25)) / 0.25)
#         z_idx = int((self.pos[2] + (size * 0.25)) / 0.25)
#         # Clamp indices to stay within grid bounds
#         x_idx = max(0, min(x_idx, size * 2))
#         z_idx = max(0, min(z_idx, size * 2))
#         idx = (x_idx) * (size * 2 + 1) + (z_idx)
#         # Apply gravitational pull toward the grid's deformation
#         target_y = grid[idx][1]
#         self.vel[1] += 0.02 * (target_y - self.pos[1])  # Gentler pull
#         # Add centripetal force to keep it orbiting
#         r = np.sqrt(self.pos[0]**2 + self.pos[2]**2)
#         if r > 0.5:  # Avoid division by zero near center
#             self.vel[0] -= 0.005 * self.pos[0] / r  # Weaker centripetal force
#             self.vel[2] -= 0.005 * self.pos[2] / r
#         # Limit y-position to stay above grid
#         self.pos[1] = max(self.pos[1] + self.vel[1], grid[idx][1] - 0.1)
#         # Correct position update
#         self.pos += self.vel
#         # Keep satellite within grid bounds in x and z
#         grid_bound = size * 0.25
#         self.pos[0] = max(-grid_bound, min(grid_bound, self.pos[0]))
#         self.pos[2] = max(-grid_bound, min(grid_bound, self.pos[2]))

#     def draw(self):
#         glPushMatrix()
#         glColor3f(1, 0, 0)  # Red satellite
#         glTranslatef(*self.pos)
#         quad = gluNewQuadric()
#         gluSphere(quad, 0.2, 16, 16)
#         glPopMatrix()

# # Initialize objects
# grid = create_grid()
# deformed_grid = deform_grid(grid)
# satellite = Satellite()
# angle = 0

# # Main loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()

#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glPushMatrix()
#     glRotatef(angle, 0, 1, 0)  # Rotate around Y-axis
    
#     draw_grid(deformed_grid)
#     draw_earth()
#     satellite.update(deformed_grid)
#     satellite.draw()
    
#     glPopMatrix()
#     angle += 0.5
#     pygame.display.flip()
#     pygame.time.wait(10)




# import pygame
# from pygame.locals import *
# from OpenGL.GL import *
# from OpenGL.GLU import *
# import numpy as np

# # Initialize Pygame and OpenGL
# pygame.init()
# display = (800, 600)
# pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
# glEnable(GL_DEPTH_TEST)
# glEnable(GL_BLEND)  # Enable blending for transparency
# glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
# glClearColor(0, 0, 0, 1)

# # Set up the camera
# gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
# glTranslatef(0, 0, -40)  # Move camera back and down to see the full grid

# # Enable lighting for 3D effect
# glEnable(GL_LIGHTING)
# glEnable(GL_LIGHT0)
# glEnable(GL_COLOR_MATERIAL)
# light_position = [0, 10, 10, 1]  # Light above and in front
# glLightfv(GL_LIGHT0, GL_POSITION, light_position)

# # Define multiple celestial bodies
# class CelestialBody:
#     def __init__(self, x, z, mass, color, radius):
#         self.pos = np.array([x, -10, z], dtype=float)  # Start below grid
#         self.mass = mass
#         self.color = color
#         self.radius = radius

#     def draw(self):
#         glPushMatrix()
#         glColor3f(*self.color)
#         glTranslatef(*self.pos)
#         quad = gluNewQuadric()
#         gluSphere(quad, self.radius, 32, 32)
#         glPopMatrix()

# # Create celestial bodies
# bodies = [
#     CelestialBody(0, 0, 20.0, (0, 1, 1), 1.5),    # Large blue "Earth"
#     CelestialBody(5, 5, 10.0, (1, 0.5, 0), 1.0),  # Orange "planet"
#     CelestialBody(-5, -5, 15.0, (1, 1, 0), 1.2)   # Yellow "star"
# ]

# def create_grid(size=40, spacing=0.25):
#     vertices = []
#     for x in range(-size, size + 1):
#         for z in range(-size, size + 1):
#             vertices.append([x * spacing, 0, z * spacing])
#     return np.array(vertices)

# def deform_grid(vertices, bodies):
#     deformed = vertices.copy()
#     for i, vertex in enumerate(deformed):
#         x, y, z = vertex
#         total_deformation = 0
#         for body in bodies:
#             dx = x - body.pos[0]
#             dz = z - body.pos[2]
#             r = np.sqrt(dx**2 + dz**2)
#             if r < 0.5: r = 0.5  # Avoid extreme deformation
#             deformation = -1.5 * body.mass / (r + 1)  # Adjusted G for multiple bodies
#             total_deformation += deformation
#         deformed[i][1] = total_deformation
#     return deformed

# def draw_grid(vertices, size=40):
#     glDisable(GL_LIGHTING)  # Disable lighting for grid
#     # Draw as a semi-transparent surface using quads
#     glBegin(GL_QUADS)
#     glColor4f(1, 1, 1, 0.3)  # White with transparency
#     for x in range(-size, size):
#         for z in range(-size, size):
#             idx1 = (x + size) * (size * 2 + 1) + (z + size)
#             idx2 = idx1 + 1
#             idx3 = idx1 + (size * 2 + 1) + 1
#             idx4 = idx1 + (size * 2 + 1)
#             if idx3 < len(vertices):
#                 glVertex3fv(vertices[idx1])
#                 glVertex3fv(vertices[idx2])
#                 glVertex3fv(vertices[idx3])
#                 glVertex3fv(vertices[idx4])
#     glEnd()
#     # Draw grid lines on top for clarity
#     glBegin(GL_LINES)
#     glColor3f(1, 1, 1)  # White lines
#     for x in range(-size, size + 1):
#         for z in range(-size, size):
#             idx1 = (x + size) * (size * 2 + 1) + (z + size)
#             idx2 = idx1 + 1
#             if idx2 < len(vertices):
#                 glVertex3fv(vertices[idx1])
#                 glVertex3fv(vertices[idx2])
#     for z in range(-size, size + 1):
#         for x in range(-size, size):
#             idx1 = (x + size) * (size * 2 + 1) + (z + size)
#             idx2 = idx1 + (size * 2 + 1)
#             if idx2 < len(vertices):
#                 glVertex3fv(vertices[idx1])
#                 glVertex3fv(vertices[idx2])
#     glEnd()
#     glEnable(GL_LIGHTING)

# class Satellite:
#     def __init__(self, x=8, z=0):
#         self.pos = np.array([x, 0, z], dtype=float)
#         self.vel = np.array([-0.1, 0, 0.2])  # Initial velocity for orbit

#     def update(self, grid, size=40):
#         # Adjust indices based on grid size and spacing
#         x_idx = int((self.pos[0] + (size * 0.25)) / 0.25)
#         z_idx = int((self.pos[2] + (size * 0.25)) / 0.25)
#         # Clamp indices to stay within grid bounds
#         x_idx = max(0, min(x_idx, size * 2))
#         z_idx = max(0, min(z_idx, size * 2))
#         idx = (x_idx) * (size * 2 + 1) + (z_idx)
#         # Apply gravitational pull toward the combined grid deformation
#         target_y = grid[idx][1]
#         self.vel[1] += 0.02 * (target_y - self.pos[1])
#         # Add centripetal force toward the nearest body
#         nearest_body = min(bodies, key=lambda b: np.sqrt((self.pos[0] - b.pos[0])**2 + (self.pos[2] - b.pos[2])**2))
#         r = np.sqrt((self.pos[0] - nearest_body.pos[0])**2 + (self.pos[2] - nearest_body.pos[2])**2)
#         if r > 0.5:
#             self.vel[0] -= 0.008 * (self.pos[0] - nearest_body.pos[0]) / r
#             self.vel[2] -= 0.008 * (self.pos[2] - nearest_body.pos[2]) / r
#         # Add damping to stabilize orbit
#         self.vel *= 0.99
#         # Limit y-position to stay above grid
#         self.pos[1] = max(self.pos[1] + self.vel[1], grid[idx][1] - 0.1)
#         self.pos += self.vel
#         # Keep satellite within grid bounds in x and z
#         grid_bound = size * 0.25
#         self.pos[0] = max(-grid_bound, min(grid_bound, self.pos[0]))
#         self.pos[2] = max(-grid_bound, min(grid_bound, self.pos[2]))

#     def draw(self):
#         glPushMatrix()
#         glColor3f(1, 0, 0)  # Red satellite
#         glTranslatef(*self.pos)
#         quad = gluNewQuadric()
#         gluSphere(quad, 0.2, 16, 16)
#         glPopMatrix()

# # Initialize objects
# grid = create_grid()
# deformed_grid = deform_grid(grid, bodies)
# satellite = Satellite()
# angle = 0

# # Main loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()

#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glPushMatrix()
#     glRotatef(angle, 0, 1, 0)  # Rotate around Y-axis
    
#     draw_grid(deformed_grid)
#     for body in bodies:
#         body.draw()
#     satellite.update(deformed_grid)
#     satellite.draw()
    
#     glPopMatrix()
#     angle += 0.5
#     pygame.display.flip()
#     pygame.time.wait(10)




import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Initialize Pygame and OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glEnable(GL_DEPTH_TEST)
glClearColor(0, 0, 0, 1)

# Set up the camera
gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
glTranslatef(0, -5, -30)  # Move camera back and down to see the full grid

# Enable lighting for 3D effect
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_COLOR_MATERIAL)
light_position = [0, 10, 10, 1]  # Light above and in front
glLightfv(GL_LIGHT0, GL_POSITION, light_position)

# Define multiple celestial bodies
class CelestialBody:
    def __init__(self, x, z, mass, color, radius):
        self.pos = np.array([x, 0, z], dtype=float)  # Position on grid level
        self.mass = mass
        self.color = color
        self.radius = radius

    def draw(self):
        glPushMatrix()
        glColor3f(*self.color)
        glTranslatef(*self.pos)
        quad = gluNewQuadric()
        gluSphere(quad, self.radius, 32, 32)
        glPopMatrix()

# Create celestial bodies
bodies = [
    CelestialBody(0, 0, 5.0, (0, 1, 1), 1.5),    # Blue "Earth"
    CelestialBody(5, 5, 3.0, (1, 0.5, 0), 1.0),  # Orange "planet"
    CelestialBody(-5, -5, 4.0, (1, 1, 0), 1.2)   # Yellow "star"
]

def create_grid(size=40, spacing=0.25):
    vertices = []
    for x in range(-size, size + 1):
        for z in range(-size, size + 1):
            vertices.append([x * spacing, 0, z * spacing])
    return np.array(vertices)

def deform_grid(vertices, bodies):
    deformed = vertices.copy()
    for i, vertex in enumerate(deformed):
        x, y, z = vertex
        total_deformation = 0
        for body in bodies:
            dx = x - body.pos[0]
            dz = z - body.pos[2]
            r = np.sqrt(dx**2 + dz**2)
            if r < 0.5: r = 0.5  # Avoid extreme deformation
            # Use a Gaussian falloff for smoother warping
            deformation = -0.1 * body.mass * np.exp(-r * r / 10.0)
            total_deformation += deformation
        deformed[i][1] = total_deformation
    return deformed

def draw_grid(vertices, size=40):
    glDisable(GL_LIGHTING)  # Disable lighting for grid
    glBegin(GL_LINES)
    glColor3f(1, 1, 1)  # White grid
    # Draw horizontal lines (along z-axis)
    for x in range(-size, size + 1):
        for z in range(-size, size):
            idx1 = (x + size) * (size * 2 + 1) + (z + size)
            idx2 = idx1 + 1
            if idx2 < len(vertices):
                glVertex3fv(vertices[idx1])
                glVertex3fv(vertices[idx2])
    # Draw vertical lines (along x-axis)
    for z in range(-size, size + 1):
        for x in range(-size, size):
            idx1 = (x + size) * (size * 2 + 1) + (z + size)
            idx2 = idx1 + (size * 2 + 1)
            if idx2 < len(vertices):
                glVertex3fv(vertices[idx1])
                glVertex3fv(vertices[idx2])
    glEnd()
    glEnable(GL_LIGHTING)

class Satellite:
    def __init__(self, x=8, z=0):
        self.pos = np.array([x, 0, z], dtype=float)
        self.vel = np.array([-0.1, 0, 0.2])  # Initial velocity for orbit

    def update(self, grid, size=40):
        # Adjust indices based on grid size and spacing
        x_idx = int((self.pos[0] + (size * 0.25)) / 0.25)
        z_idx = int((self.pos[2] + (size * 0.25)) / 0.25)
        # Clamp indices to stay within grid bounds
        x_idx = max(0, min(x_idx, size * 2))
        z_idx = max(0, min(z_idx, size * 2))
        idx = (x_idx) * (size * 2 + 1) + (z_idx)
        # Apply gravitational pull toward the combined grid deformation
        target_y = grid[idx][1]
        self.vel[1] += 0.02 * (target_y - self.pos[1])
        # Add centripetal force toward the nearest body
        nearest_body = min(bodies, key=lambda b: np.sqrt((self.pos[0] - b.pos[0])**2 + (self.pos[2] - b.pos[2])**2))
        r = np.sqrt((self.pos[0] - nearest_body.pos[0])**2 + (self.pos[2] - nearest_body.pos[2])**2)
        if r > 0.5:
            self.vel[0] -= 0.008 * (self.pos[0] - nearest_body.pos[0]) / r
            self.vel[2] -= 0.008 * (self.pos[2] - nearest_body.pos[2]) / r
        # Add damping to stabilize orbit
        self.vel *= 0.99
        # Limit y-position to stay above grid
        self.pos[1] = max(self.pos[1] + self.vel[1], grid[idx][1] - 0.1)
        self.pos += self.vel
        # Keep satellite within grid bounds in x and z
        grid_bound = size * 0.25
        self.pos[0] = max(-grid_bound, min(grid_bound, self.pos[0]))
        self.pos[2] = max(-grid_bound, min(grid_bound, self.pos[2]))

    def draw(self):
        glPushMatrix()
        glColor3f(1, 0, 0)  # Red satellite
        glTranslatef(*self.pos)
        quad = gluNewQuadric()
        gluSphere(quad, 0.2, 16, 16)
        glPopMatrix()

# Initialize objects
grid = create_grid()
deformed_grid = deform_grid(grid, bodies)
satellite = Satellite()
angle = 0

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(angle, 0, 1, 0)  # Rotate around Y-axis
    
    draw_grid(deformed_grid)
    for body in bodies:
        body.draw()
    satellite.update(deformed_grid)
    satellite.draw()
    
    glPopMatrix()
    angle += 0.5
    pygame.display.flip()
    pygame.time.wait(10)