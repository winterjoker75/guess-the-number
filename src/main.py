import pygame
from scenes.single_play import single_play
from scenes.game_over import game_over
from scripts.game import SingleGame

if __name__=="__main__":
	pygame.init()

	screen = pygame.display.set_mode((640, 480))
	clock = pygame.time.Clock()

	game = SingleGame()
	single_play(screen, clock, game)
	game_over(screen, clock, game)
