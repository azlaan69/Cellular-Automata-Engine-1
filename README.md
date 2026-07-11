Basic Cellular Engine. Uses NumPy and Pygame.
Currently has 4 material types:
  Sand: Falls straight down
  Stone: Stays anchored where it's placed
  Water: Falls straight down until it gets stopped, then flows left/right.
  Acid: Falls straight down and breaks everything in it's way
Controls:
  LMB: Place material
  RMB: Switch material (1-4)

Params:
  Game speed can be changed by modifying line 89 "clock.tick(60)". The higher the value, the faster.
  Grid Size can be changed by modifying line 23 "gridSize = 50". The higher the value, the more grid rows/columns.
  Screen resolution can be changed by modifying line 16 "screensize = 400".
