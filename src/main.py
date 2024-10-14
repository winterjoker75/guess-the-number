import pygame
from scenes.main_menu import main_menu

if __name__=="__main__":
	pygame.init()

	screen = pygame.display.set_mode((640, 480))
	clock = pygame.time.Clock()

	main_menu(screen, clock)
