import numpy as np
import random
import pygame
import pygame._sdl2.video as sdl2_video
import sys

palette = np.array([
    [0, 0, 0],        # air idx 0
    [255, 200, 100],  # sand idx 1
    [150, 150, 150],  # stone idx 2
    [0, 0, 255],      # water idx 3
    [0, 255, 0]       # acid idx 4
], dtype=np.uint8)

pygame.init()
screensize = 400
screen = pygame.display.set_mode((screensize, screensize))
pygame.display.set_caption("Sandbox")
window = sdl2_video.Window.from_display_module()
window.always_on_top = True
clock = pygame.time.Clock()

gridSize = 50
grid = np.zeros((gridSize, gridSize), dtype=np.uint8)
cellSize = screensize // gridSize
currentMaterial = 1

subsurf = pygame.Surface((gridSize, gridSize))

running = True

while running:

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_F12: running = False
		elif event.type == pygame.QUIT: running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 3:
				if currentMaterial < 4: currentMaterial += 1
				else: currentMaterial = 1
	
	mouseX, mouseY = pygame.mouse.get_pos()
	mouseButtons = pygame.mouse.get_pressed()

	gridX = mouseX // cellSize
	gridY = mouseY // cellSize

	if 0 <= gridX < gridSize and 0 <= gridY < gridSize:
		if mouseButtons[0]:
			grid[gridY, gridX] = currentMaterial

	acidfallMask = (grid[:-1, :] == 4)
	waterfallMask = (grid[:-1, :] == 3) & (grid[1:, :] == 0)
	waterRightMask = (grid[:-1, :-1] == 3) & (grid[:-1, 1:] == 0) & (grid[1:, :-1] != 0)
	waterLeftMask = (grid[:-1, 1:] == 3) & (grid[:-1, :-1] == 0) & (grid[1:, 1:] != 0)
	fallMask = (grid[:-1, :] == 1) & (grid[1:, :] == 0)

	sandMask = (grid == 1)
	stoneMask = (grid == 2)
	waterMask = (grid == 3)
	acidMask = (grid == 4)

	grid[:-1, :][fallMask] = 0
	grid[1:, :][fallMask] = 1

	grid[:-1, :][waterfallMask] = 0
	grid[1:, :][waterfallMask] = 3	

	bottom = grid[-1, :]
	bottom[bottom == 4] = 0

	if random.choice([True, False]):
		grid[:-1, :-1][waterRightMask] = 0
		grid[:-1, 1:][waterRightMask] = 3	
	else: 
		grid[:-1, 1:][waterLeftMask] = 0
		grid[:-1, :-1][waterLeftMask] = 3	

	grid[:-1, :][acidfallMask] = 0
	grid[1:, :][acidfallMask] = 4

	cGrid = palette[grid.astype(np.uint8).T]
	pygame.surfarray.blit_array(subsurf, cGrid)
	pygame.transform.scale(subsurf, (screensize, screensize), screen)
	pygame.display.flip()
 
	clock.tick(60)

pygame.quit()
sys.exit() 