import pygame as py
import sys

sys.setrecursionlimit(1500)

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

def fill(object, color, actual_color):
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
color_objects.append(grid(1015, 25, 75, "green"))
color_objects.append(grid(1100, 25, 75, "red"))
color_objects.append(grid(1015, 110, 75, "blue"))
color_objects.append(grid(1100, 110, 75, "yellow"))
color_objects.append(grid(1015, 195, 75, "pink"))
color_objects.append(grid(1100, 195, 75, "brown"))
color_objects.append(grid(1015, 280, 75, "white"))
color_objects.append(grid(1100, 280, 75, "black"))

def main():
    win.fill((13, 21, 133))
    running = True
    for obj in grid_objects:
        obj.draw()
    py.draw.rect(win, "green", (1015, 25, 75, 75))
    py.draw.rect(win, "red", (1100, 25, 75, 75))
    py.draw.rect(win, "blue", (1015, 110, 75, 75))
    py.draw.rect(win, "yellow", (1100, 110, 75, 75))
    py.draw.rect(win, "pink", (1015, 195, 75, 75))
    py.draw.rect(win, "brown", (1100, 195, 75, 75))
    py.draw.rect(win, "white", (1015, 280, 75, 75))
    py.draw.rect(win, "black", (1100, 280, 75, 75))

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

                        py.display.update(obj.x, obj.y, obj.size, obj.size)
                for obj in color_objects:
                    if py.Rect.collidepoint(obj.return_rect(), py.mouse.get_pos()):
                        color = obj.color
   
            if py.mouse.get_pressed()[2]:
                for obj in grid_objects:
                    if py.Rect.collidepoint(obj.return_rect(), py.mouse.get_pos()):
                        fill(obj, color, obj.color)
                        # obj.color = "white"
                        # obj.draw()
                        py.display.update(obj.x, obj.y, obj.size, obj.size)
            if py.mouse.get_pressed()[1]:
                for obj in grid_objects:
                    obj.color = color
                    obj.draw()
                py.display.flip()

        # for obj in grid_objects:
        #     py.display.update(obj.x, obj.y, obj.size, obj.size)
        py.display.flip()
        clock.tick(300)
        print(clock.get_fps())
    quit()
main()
