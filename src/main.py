import pygame
from scenes.single_play import single_play

if __name__=="__main__":
	pygame.init()

	screen = pygame.display.set_mode((640, 480))
	clock = pygame.time.Clock()

	single_play(screen, clock)
