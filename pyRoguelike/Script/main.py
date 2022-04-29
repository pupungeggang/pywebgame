import sys
import pygame

import var

def main():
    pygame.init()
    var.screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Desserterria Roguelike')
    var.clock = pygame.time.Clock()

    while True:
        loop()

def loop():
    var.clock.tick(var.FPS)
    loop_scene()
    input_handle()

def loop_scene():
    pass

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

main()
    
