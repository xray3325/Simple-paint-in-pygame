import pygame as py
import sys

sys.setrecursionlimit(15000)

py.init()

WIDTH = 1200
HEIGHT = 800
win = py.display.set_mode((WIDTH, HEIGHT))
clock = py.time.Clock()

class grid():
    def __init__(self, x, y, width, color="white"):
        self.x = x
        self.y = y
        self.size = width
        self.color = color

    def draw(self):
        py.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))

    def return_rect(self):
        rect = py.Rect(self.x, self.y, self.size, self.size)
        return rect

def count(object, color, iterations):
    if iterations > 0:
        lista = thickness(object, color)
        for obj in lista:
            count(obj, color, iterations-1)

    else:
        object.color = color
        object.draw()

def thickness(object, color):
    obiekty = []
    for obj in grid_objects:
            if obj.color != color:
                if  obj.x == object.x + size and obj.y == object.y or \
                    obj.x == object.x - size and obj.y == object.y or \
                    obj.x == object.x and obj.y == object.y + size or \
                    obj.x == object.x and obj.y == object.y - size or \
                    obj == object:

                    obiekty.append(obj)
    return(obiekty)

def fill(object, color, actual_color ):
    for obj in grid_objects:
        if obj.color == actual_color:
                if obj.color != color:
                    if obj.x == object.x + size and obj.y == object.y or \
                        obj.x == object.x - size and obj.y == object.y or \
                        obj.x == object.x and obj.y == object.y + size or \
                        obj.x == object.x and obj.y == object.y - size or \
                        obj == object:
                        obj.color = color
                        obj.draw()
                        fill(obj, color, actual_color)

grid_objects = []
size = 25
for i in range(25, WIDTH-size*9, size):
    for j in range(25, HEIGHT-size, size):
        grid_objects.append(grid(i, j, size))

color_objects = []
color_objects.append(grid(995, 25, 90, "green"))
color_objects.append(grid(1090, 25, 90, "red"))
color_objects.append(grid(995, 120, 90, "blue"))
color_objects.append(grid(1090, 120, 90, "yellow"))
color_objects.append(grid(995, 215, 90, "pink"))
color_objects.append(grid(1090, 215, 90, "brown"))
color_objects.append(grid(995, 310, 90, "white"))
color_objects.append(grid(1090, 310, 90, "black"))

def main():
    fps = 200
    win.fill((13, 21, 133))
    running = True
    for obj in grid_objects:
        obj.draw()
    py.draw.rect(win, "green", (995, 25, 90, 90))
    py.draw.rect(win, "red", (1090, 25, 90, 90))
    py.draw.rect(win, "blue", (995, 120, 90, 90))
    py.draw.rect(win, "yellow", (1090, 120, 90, 90))
    py.draw.rect(win, "pink", (995, 215, 90, 90))
    py.draw.rect(win, "brown", (1090, 215, 90, 90))
    py.draw.rect(win, "white", (995, 310, 90, 90))
    py.draw.rect(win, "black", (1090, 310, 90, 90))

    py.display.flip()
    color = "red"
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            if py.mouse.get_pressed()[0]:
                for obj in grid_objects:
                    if py.Rect.collidepoint(obj.return_rect(), py.mouse.get_pos()):
                        obj.color = color
                        obj.draw()                        

                for obj in color_objects:
                    if py.Rect.collidepoint(obj.return_rect(), py.mouse.get_pos()):
                        color = obj.color
   
            if py.mouse.get_pressed()[2]:
                for obj in grid_objects:
                    if py.Rect.collidepoint(obj.return_rect(), py.mouse.get_pos()):
                        count(obj, color, 3)

            if py.mouse.get_pressed()[1]:
                for obj in grid_objects:
                    obj.color = color
                    obj.draw()

        py.display.flip()
        clock.tick(300)
        current_fps = clock.get_fps()
        if current_fps < fps:
            print(fps)
    quit()
main()
