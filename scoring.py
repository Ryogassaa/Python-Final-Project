import pygame


class Scoring:
    def __init__(self, display, point, corX, corY):
        from pong import color_white
        self.display = display
        self.point = point
        self.corX = corX
        self.corY = corY
        self.font = pygame.font.SysFont("monospace", 80, bold=True)  # Chosen Font
        self.tag = self.font.render(self.point, 0, color_white)      # render points
        self.draw_score()

    # Display the score to the game
    def draw_score(self):
        self.display.blit(self.tag, (self.corX - self.tag.get_rect().width // 2, self.corY))

    # Adds the score by 1
    def add_score(self):
        from pong import color_white
        point = int(self.point) + 1
        self.point = str(point)
        self.tag = self.font.render(self.point, 0, color_white)

    # Restart to 0 points from any points
    def game_restart(self):
        from pong import color_white
        self.point = '0'
        self.tag = self.font.render(self.point, 0, color_white)
